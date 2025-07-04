const project_loader = async (folderPath) => {
    const container = document.getElementById("information_about_member");

    container.innerHTML = `
        <h2>Code 😎</h2>
        <div class="project-files-flex">
            <ul id="file-list"></ul>
            <pre id="code-container"></pre>
        </div>
    `;

    const fileListElement = document.getElementById("file-list");
    const codeContainer = document.getElementById("code-container");

    try {
        const indexRes = await fetch(`${folderPath}/index.json`);
        if (!indexRes.ok) throw new Error(`index.json not found in ${folderPath}`);
        const files = await indexRes.json();

        files.forEach(filename => {
            const li = document.createElement("li");
            li.textContent = filename;
            li.addEventListener("click", async () => {
                try {
                    const fileRes = await fetch(`${folderPath}/${filename}`);
                    if (!fileRes.ok) throw new Error(`Failed to load ${filename}`);
                    const content = await fileRes.text();
                    codeContainer.textContent = content;
                } catch (err) {
                    codeContainer.textContent = "Error loading file: " + err.message;
                }
            });
            fileListElement.appendChild(li);
        });
    } catch (err) {
        codeContainer.textContent = "Error loading project: " + err.message;
        console.error(err);
    }
};

export default project_loader;
