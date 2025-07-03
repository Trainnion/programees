import members from "./members.js";


const show_projects = (member_ID) => {
    
    let content = document.getElementById("content");
    content.innerHTML = "";
    let information_about_member= document.createElement("div");
    information_about_member.className = "information_about_member";
    content.appendChild(information_about_member);
    let member_message = document.createElement("p");

    for (let member of members) {
        if (member.id === member_ID) {
            member_message.textContent = member.message;
            information_about_member.appendChild(member_message);
        }
    }
    

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
            show_projects(member.id);
        };
    }
}

window.show_members = show_members;

show_members();





















