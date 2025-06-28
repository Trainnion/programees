

let members = [
    owen = {
        name: "Owen S. Estrera \"Nataho\"",
        profile_picture: "./members/estrera.jpg",
        projects: [
            {
                name: "programees",
                description: "A platform for programmers to collaborate and share knowledge.",
            }
        ]
    },

    cornelius = {
        name: "Cornelius Timosa II \"Coke addict\"",
        profile_picture: "./members/timosa.jpg",
        projects: [
            {
                name: "projectX",
                description: "A groundbreaking project that changes everything.",
            }
        ]
    },

    denise = {
        name: "Adrianne Caballero  \"DEN\"",
        profile_picture: "./members/dennise.jpg",
        projects: [
            {
                name: "projectY",
                description: "An innovative project that pushes boundaries.",
            }
        ]
    }
]


//creating member_cards
let content = document.getElementById("content");
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

    // let projectList = document.createElement("ul");
    // for (let project of member.projects) {
    //     let projectItem = document.createElement("li");
    //     projectItem.textContent = `${project.name}: ${project.description}`;
    //     projectList.appendChild(projectItem);
    // }
    // memberDiv.appendChild(projectList);

    content.appendChild(memberDiv);
}