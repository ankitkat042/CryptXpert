document.addEventListener("DOMContentLoaded", function () {
    const symmetricAlgos = document.getElementById("symmetric-algos");
    const asymmetricAlgos = document.getElementById("asymmetric-algos");
    const hashAlgos = document.getElementById("hash-algos");
    const algoTitle = document.getElementById("algo-title");
    const algoDescription = document.getElementById("algo-description");

    // Algorithm categories
    const algorithms = {
        symmetric: ["AES", "DES", "Triple DES", "Blowfish", "RC4"],
        asymmetric: ["RSA", "El Gamal"],
        hash: ["MD5", "SHA256", "SHA512"],
    };

    const endpointName = new Map([
        ["AES", "aes"],
        ["DES", "des"],
        ["Triple DES", "3des"],
        ["Blowfish", "blowfish"],
        ["RC4", "rc4"],
        ["RSA", "rsa"],
        ["El Gamal", "elgamal"],
        ["MD5", "md5"],
        ["SHA256", "sha256"],
        ["SHA512", "sha512"],
    ]);

    // Populate the algorithm lists by category
    function populateAlgoList(category, listElement) {
        algorithms[category].forEach((algo) => {
            const li = document.createElement("li");
            li.textContent = algo;
            li.addEventListener("click", () => loadAlgorithm(category, algo));
            listElement.appendChild(li);
        });
    }

    // Populate all categories
    populateAlgoList("symmetric", symmetricAlgos);
    populateAlgoList("asymmetric", asymmetricAlgos);
    populateAlgoList("hash", hashAlgos);

    // Load algorithm details when clicked
    function loadAlgorithm(category, algo) {
        algoTitle.textContent = algo;
        if (category === "symmetric") {
            algoDescription.innerHTML = `
                <div class="form-group">
                    <label for="plain-text">Plain Text(HEX)</label>
                    <input type="text" id="plaintext-input" placeholder="Enter plain text for encryption otherwise leave blank for decryption">
                </div>
                <div class="form-group">
                    <label for="key">Key(HEX)</label>
                    <input type="text" id="key-input" placeholder="Enter symmetric key">
                </div>
                ${checkTripleDES(algo)}
                <div class="form-group">
                    <label for="key">Cipher Text</label>
                    <input type="text" id="ciphertext-input" placeholder="Enter cipher text for decryption otherwise leave blank for encryption">
                </div>
                <div class="buttons">
                    <button onclick="encrypt('${algo}')">Encrypt</button>
                    <button onclick="decrypt('${algo}')">Decrypt</button>
                </div>
            `;
        } else if (category === "asymmetric") {
            algoDescription.innerHTML = `
            <div class="form-group">
                <label for="keysize-input">Key Size</label>
                <input type="text" id="keysize-input" placeholder="Enter ${algo} key size">
            </div>
            <div class="buttons">
                <button onclick="generateKeys('${algo}')">Generate Keys</button>
            </div>
            <div class="form-group">
                <label for="publickey-input">Public Key</label>
                <input type="text" id="publickey-input" placeholder="Enter public key otherwise leave blank for generation">
            </div>
            <div class="form-group">
                <label for="privatekey-input">Private Key</label>
                <input type="text" id="privatekey-input" placeholder="Enter private key otherwise leave blank for generation">
            </div>
            <div class="form-group">
                <label for="plain-text">Plain Text</label>
                <input type="text" id="plaintext-input" placeholder="Enter plain text for encryption otherwise leave blank for decryption">
            </div>
            <div class="form-group">
                <label for="key">Cipher Text</label>
                <input type="text" id="ciphertext-input" placeholder="Enter cipher text for decryption otherwise leave blank for encryption">
            </div>
            <div class="buttons">
                <button onclick="encryptAssymetric('${algo}')">Encrypt</button>
                <button onclick="decryptAssymetric('${algo}')">Decrypt</button>
            </div>
            `;
        } else if (category === "hash") {
            algoDescription.innerHTML = `
                <div class="form-group">
                    <label for="message-input">Message</label>
                    <input type="text" id="message-input" placeholder="Enter message to hash">
                </div>
                <div class="form-group">
                    <label for="hash-input">Hash</label>
                    <input type="text" id="hash-input" placeholder="Hash will appear here" disabled>
                </div>
                <div class="buttons">
                    <button onclick="hash('${algo}')">Hash</button>
                </div>
            `;
        }
    }
    
    window.encryptAssymetric = function (algo) {
        const publicKey = document.getElementById("publickey-input").value;
        const plaintext = document.getElementById("plaintext-input").value;
        if (!publicKey || !plaintext) {
            alert("Please provide both public key and plaintext.");
            return;
        }
        data = {
            plaintext: plaintext,
            public_key: publicKey,
        };

        sendPostRequest(data, `/crypto/${endpointName.get(algo)}/encrypt/`, (response) => {
            if (response && response.ciphertext) {
                document.getElementById("ciphertext-input").value = response.ciphertext;
            } else {
                alert("Encryption failed, no ciphertext returned.");
            }
        });
    };

    window.decryptAssymetric = function (algo) {
        const privateKey = document.getElementById("privatekey-input").value;
        const ciphertext = document.getElementById("ciphertext-input").value;
        if (!privateKey || !ciphertext) {
            alert("Please provide both private key and ciphertext.");
            return;
        }
        data = {
            ciphertext: ciphertext,
            private_key: privateKey,
        };

        sendPostRequest(data, `/crypto/${endpointName.get(algo)}/decrypt/`, (response) => {
            if (response && response.plaintext) {
                document.getElementById("plaintext-input").value = response.plaintext;
            } else {
                alert("Encryption failed, no plaintext returned.");
            }
        });
    };


    window.encrypt = function (algo) {
        const key = document.getElementById("key-input").value;
        const plaintext = document.getElementById("plaintext-input").value;
        if (!key || !plaintext) {
            alert("Please provide both key and plaintext.");
            return;
        }
        data = {
            plaintext: plaintext,
        };

        if (algo === "Triple DES") {
            const key2 = document.getElementById("key2-input").value;
            if (!key2) {
                alert("Please provide second key.");
                return;
            }
            data.key1 = key;
            data.key2 = key2;
        } else {
            data.key = key;
        }

        sendPostRequest(data, `/crypto/${endpointName.get(algo)}/encrypt/`, (response) => {
            if (response && response.ciphertext) {
                document.getElementById("ciphertext-input").value = response.ciphertext;
            } else {
                alert("Encryption failed, no ciphertext returned.");
            }
        });
    };

    window.decrypt = function (algo) {
        const key = document.getElementById("key-input").value;
        const ciphertext = document.getElementById("ciphertext-input").value;
        if (!key || !ciphertext) {
            alert("Please provide both key and ciphertext.");
            return;
        }

        data = {
            ciphertext: ciphertext,
        };

        if (algo === "Triple DES") {
            const key2 = document.getElementById("key2-input").value;
            if (!key2) {
                alert("Please provide second key.");
                return;
            }
            data.key1 = key;
            data.key2 = key2;
        } else {
            data.key = key;
        }

        sendPostRequest(data, `/crypto/${endpointName.get(algo)}/decrypt/`, (response) => {
            if (response && response.plaintext) {
                document.getElementById("plaintext-input").value = response.plaintext;
            } else {
                alert("Encryption failed, no plaintext returned.");
            }
        });
    };

    window.generateKeys = function(algo) {
        const keySize = document.getElementById("keysize-input").value;
        if (!keySize) {
            alert("Please provide key size.");
            return;
        }

        const data = {
            key_size: keySize
        };

        sendPostRequest(data, `/crypto/${endpointName.get(algo)}/generate_keys/`, (response) => {
            if (response && response.public_key, response.private_key) {
                document.getElementById("publickey-input").value = response.public_key;
                document.getElementById("privatekey-input").value = response.private_key;
            } else {
                alert("Encryption failed, no public-private key pair returned.");
            }
        });
    }

    window.hash = function (algo) {
        const message = document.getElementById("message-input").value;
        if (!message) {
            alert("Please provide message for hashing.");
            return;
        }
        data = {
            message: message,
        };

        sendPostRequest(data, `/crypto/${endpointName.get(algo)}/`, (response) => {
            if (response && response.hash) {
                document.getElementById("hash-input").value = response.hash;
            } else {
                alert("Encryption failed, no hash returned.");
            }
        });
    };
});

function rsaUI() {
    return `
        <div class="form-group">
            <label for="keysize-input">Key Size(eg. 512)</label>
            <input type="text" id="keysize-input" placeholder="Enter RSA key size">
        </div>
        <div class="buttons">
            <button onclick="rsaGenerateKeys()">Generate Keys</button>
        </div>
        <div class="form-group">
            <label for="publickey-input">Public Key</label>
            <input type="text" id="publickey-input" placeholder="Enter public key otherwise leave blank for generation">
        </div>
        <div class="form-group">
            <label for="privatekey-input">Private Key</label>
            <input type="text" id="privatekey-input" placeholder="Enter private key otherwise leave blank for generation">
        </div>
        <div class="form-group">
            <label for="plain-text">Plain Text</label>
            <input type="text" id="plaintext-input" placeholder="Enter plain text for encryption otherwise leave blank for decryption">
        </div>
        <div class="form-group">
            <label for="key">Cipher Text</label>
            <input type="text" id="ciphertext-input" placeholder="Enter cipher text for decryption otherwise leave blank for encryption">
        </div>
        <div class="buttons">
            <button onclick="encrypt('RSA')">Encrypt</button>
            <button onclick="decrypt('RSA')">Decrypt</button>
        </div>
    `;
}

function checkTripleDES(algo) {
    if (algo === "Triple DES") {
        return `
            <div class="form-group">
                <label for="key">Key 2</label>
                <input type="text" id="key2-input" placeholder="Enter second symmetric key">
            </div>
        `;
    } else return "";
}

function sendPostRequest(data, endpoint, successAction) {
    function getCSRFToken() {
        const cookies = document.cookie.split("; ");
        for (const cookie of cookies) {
            const [name, value] = cookie.split("=");
            if (name === "csrftoken") {
                console.log("CSRF Token:", value);
                return value;
            }
        }
        return "";
    }
    fetch(endpoint, {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
            "X-CSRFToken": getCSRFToken(),
        },
        body: JSON.stringify(data),
    })
        .then((response) => {
            if (!response.ok) {
                return response.json().then((data) => {
                    throw new Error(`HTTP error! status: ${response.status}, message: ${data.error}`);
                });
            }
            console.log(response);
            return response.json();
        })
        .then((response) => {
            successAction(response);
        })
        .catch((error) => {
            alert(error);
        });
}
