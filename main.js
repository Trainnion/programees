import members from "./Programees_members.js";
const languages = [
    "JavaScript",
    "Python",  
    "C++",
    "Java",
    "C#",
    "Godot",
];


const show_project_information = (viewed_project) => {
    let information_about_member = document.getElementById("information_about_member");

    const existing_project_infomation = document.getElementById("project_information");
    if (existing_project_infomation) {
        existing_project_infomation.remove();
    }
    let project_information = document.createElement("div");
    project_information.className = "project_information";
    project_information.id = "project_information";
    information_about_member.appendChild(project_information);

    let project_message = document.createElement("h5");
    project_message.textContent = viewed_project.description || "This is a placeholder for project information.";
    project_information.appendChild(project_message);

    // Create a play button with play_arrow image if a Filedirectory exists
    if (viewed_project.File_directory) {
        let playButton = document.createElement("button");
        playButton.className = "play_button";
        let playIcon = document.createElement("img");
        playIcon.src = "./assets/buttons/play_arrow.svg";
        playIcon.alt = "Play";
        playButton.appendChild(playIcon);
        playButton.onclick = () => {
            console.log("hello");
        };
        project_information.appendChild(playButton);
    }
    // You can add more details about the project here
}

const show_member_information = (member_ID) => {
    let content = document.getElementById("content");
    content.innerHTML = "";
    let information_about_member = document.createElement("div");
    information_about_member.className = "information_about_member";
    information_about_member.id = "information_about_member";
    content.appendChild(information_about_member);
    let member_message = document.createElement("p");

    let viewed_member = members.find(member => member.id === member_ID);
    if (viewed_member) {
        member_message.textContent = viewed_member.message;
        information_about_member.appendChild(member_message);
    }

   
    const title = document.createElement("h3");
    title.textContent = "My Projects...";
    information_about_member.appendChild(title);

    let list_of_languages = document.createElement("div");
    list_of_languages.className = "list_of_languages";
    information_about_member.appendChild(list_of_languages);

    // Only show languages that have at least one project
    languages.forEach(language => {
        const projectsForLanguage = viewed_member.projects.filter(project => project.language === language);
        if (projectsForLanguage.length > 0) {
            let languageElement = document.createElement("ul");
            languageElement.className = "language";
            // Add language name as a heading
            let langTitle = document.createElement("strong");
            langTitle.textContent = language;
            languageElement.appendChild(langTitle);
            // List projects for this language
            projectsForLanguage.forEach(project => {
                let projectElement = document.createElement("li");
                projectElement.className = "project";
                projectElement.textContent = project.name;
                languageElement.appendChild(projectElement);

                projectElement.onclick = () => {
                    show_project_information(project);
                };
            });
            list_of_languages.appendChild(languageElement);
        }
    });
}

export const show_members = () => {
    let content = document.getElementById("content");
    content.innerHTML = "";
    //creating member_cards
    for (let member of members) {
        let memberDiv = document.createElement("div");
        memberDiv.className = "member_container"

        let profilePicture = document.createElement("img");
        profilePicture.src = member.profile_picture;
        profilePicture.alt = "Profile Picture";
        memberDiv.appendChild(profilePicture);

        let name = document.createElement("h2");
        name.textContent = member.name;
        memberDiv.appendChild(name);

        content.appendChild(memberDiv);


        memberDiv.onclick = () => {
            show_member_information(member.id);
        };
    }
}

window.show_members = show_members;

show_members();





















