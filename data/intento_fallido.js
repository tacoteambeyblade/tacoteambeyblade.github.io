const COMMUNITY_ID = "PlazaCoacalco"

function makeGetRequest(){
    //Get values from UI
    const api_key = document.getElementById("apikey").value.trim();
    const tournament_id = document.getElementById("tournamentid").value.trim();

    //Build the URL
    const challonge_url = `https://api.challonge.com/v2.1/communities/${COMMUNITY_ID}/tournaments/${tournament_id}/matches.json`

    //Build the headers
    const headers = new Headers();
    headers.append("Accept", "application/json");
    headers.append("Content-Type", "application/vnd.api+json");
    headers.append("Authorization-Type", "v1");
    headers.append("Authorization", api_key);
    headers.append("If-None-Match", "");

    //Build the options
    const request_options = {
        method: "GET",
        headers: headers,
        redirect: "follow"
    };

    //Make the request
    fetch(challonge_url, request_options)
    .then((response) => response.text())
    .then((result) => console.log(result))
    .catch((error) => console.error(error));
    
    //Print the values
    headers.forEach((valor, nombre) => {
        console.log(`${nombre}: ${valor}`);
    });
    console.log(`APIKEY: ${api_key} tournamentid: ${tournament_id}`);
    console.log(`URL: ${challonge_url}`)

}; 

document.getElementById("request").addEventListener("click", makeGetRequest);