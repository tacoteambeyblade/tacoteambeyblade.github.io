import BLADERS from "../data/bladers.json" with { type: "json"}

function sortRanking(){
    // ... spread operator to not modify the original values
    // uses - due sort only uses positive and negative values not booleans
    const bladers = BLADERS["bladers"]
    const ranking = [...bladers].sort((a,b) => b.score_tc - a.score_tc)

    const container = document.getElementById("ranking");

    ranking.forEach((blader, index) =>{
        console.log(`${index+1}. ${blader.names[0]} -> ${blader.score_tc}`)
    })

    let shared_ranking = []
    let curent = 1
    let past = null 

    ranking.forEach((blader, index) => {
        // Validation to avoid bladers with 0pts (0pts means blader not registered) 
        if(blader.score_tc <= 0) return
        // Validation to avoid non taco bladers 
        if(blader.is_taco == 0) return

        if(blader.score_tc !== past){
            curent = index+1
            past = blader.score_tc
        }

        shared_ranking.push({curent, ...blader})

        // Creates the dom elements
        const item = document.createElement("div");
        item.classList.add("blader");

        item.innerHTML = `
            <strong>${curent}. Taco de ${blader.taco_name.toUpperCase()}</strong>
            <span>${blader.score_tc} pts</span>
        `;

        container.appendChild(item);
    })

    
}

sortRanking()