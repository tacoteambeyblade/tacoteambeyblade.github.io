import BLADERS from "../data/bladers.json" with { type: "json"}

function compute_battle(){
    const bet_points    = document.getElementById("bet_points").value
    const winner_pos    = document.getElementById("winner_pos").value
    const loser_pos     = document.getElementById("loser_pos").value
    const winner_multiplier = winner_pos*bet_points
    const loser_multiplier  = loser_pos*bet_points
    console.log(`Puntos apostados: ${bet_points}`)
    console.log(`Ganador  + ${winner_multiplier} puntos`)
    console.log(`Perdedor - ${loser_multiplier}  puntos`)
    document.getElementById("winner_points").innerText = `Ganador  + ${winner_multiplier} puntos`
    document.getElementById("loser_points").innerHTML = `Perdedor - ${loser_multiplier}  puntos`
}

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

const compute_button = document.getElementById("compute_button")
compute_button.addEventListener("click", compute_battle)