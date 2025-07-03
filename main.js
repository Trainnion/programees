import members from "./members.js";

const languages = [
    "JavaScript",
    "Python",  
    "C++",
    "Java",
    "C#",
    "Godot",
]


const show_member_information = (member_ID) => {
    
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
    let list_of_languages = document.createElement("div");
    list_of_languages.className = "list_of_languages";
    information_about_member.appendChild(list_of_languages);


    for(let member of members) {
        if (member.id === member_ID) {
            for (let language of languages) {
                for(let project of member.projects) {
                    if (project.language === language) {
                        let languageElement = document.createElement("li");
                        languageElement.className = "language";
                        languageElement.textContent = language;
                        list_of_languages.appendChild(languageElement);
                    }
                 }
            }
        break;
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
            show_member_information(member.id);
        };
    }
}

window.show_members = show_members;

show_members();





















