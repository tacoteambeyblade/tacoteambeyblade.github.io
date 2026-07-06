import bladers from "../data/bladers.json" with { type: "json"}

function sortRanking(){
    // ... spread operator to not modify the original values
    // uses - due sort only uses positive and negative values not booleans
    const ranking = [...bladers].sort((a,b) => b.score_tl - a.score_tl)

    const container = document.getElementById("ranking");

    ranking.forEach((blader, index) =>{
        console.log(`${index+1}. ${blader.names[0]} -> ${blader.score_tl}`)
    })

    let shared_ranking = []
    let curent = 1
    let past = null 

    ranking.forEach((blader, index) => {
        if(blader.score_tl !== past){
            curent = index+1
            past = blader.score_tl
        }

        shared_ranking.push({curent, ...blader})

        // Creates the dom elements
        const item = document.createElement("div");
        item.classList.add("blader");

        item.innerHTML = `
            <strong>${curent}. ${blader.names[0].toUpperCase()}</strong>
            <span>${blader.score_tl} pts</span>
        `;

        container.appendChild(item);
    })

    
}

sortRanking()