

import members from "./members.js";

const show_projects = (member_ID) => {
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





















