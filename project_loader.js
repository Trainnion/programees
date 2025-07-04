const project_loader = async (folderPath, project_name) => {
    const container = document.getElementById("information_about_member");


    let existing_title = document.getElementById("Project_title");
    let existing_Project_files = document.getElementsByClassName("project-files-flex");

    //check if theres already a project being shown
    if (existing_title) {
        existing_title.remove();
    }
    if (existing_Project_files.length > 0) {
        Array.from(existing_Project_files).forEach(el => el.remove());
    }

    //creates the semi-file browser
    const title = document.createElement("h2");
    title.id = "Project_title";
    title.textContent = `${project_name}`;

    const wrapper = document.createElement("div");
    wrapper.className = "project-files-flex";

    const ul = document.createElement("ul");
    ul.id = "file-list";

    const pre = document.createElement("pre");
    pre.id = "code-container";

    wrapper.appendChild(ul);
    wrapper.appendChild(pre);
    container.appendChild(title);
    container.appendChild(wrapper);

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
