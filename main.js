

let members = [
    owen = {
        id: "00001",
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
        id: "00002",
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
        id: "00003",
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

const show_projects = (member) => {
    // alert(`Projects for ${member.name}: ${member.projects.map(p => p.name).join(", ")}`);
    let content = document.getElementById("content");
    content.innerHTML = "";
};

const show_members = () => {
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
            show_projects(member.id);
        };
    }
}

show_members();





















