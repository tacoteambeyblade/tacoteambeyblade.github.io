from pathlib import Path
import json

TOURNAMENT_TYPE = "R" #L=League, F=Fun, R=Rebels
DATE = "02" #Fecha
PART = "1" #1=single 2=double
SEASON = "B" #B=Bistec

SCORE_KEY = f"score_t{TOURNAMENT_TYPE.lower()}"
print(SCORE_KEY)

FILE_BLADERS = "../bladers.json"
FILE_RESULTS = f"T{TOURNAMENT_TYPE}F{DATE}0{PART}{SEASON}.json" #TRF0101B means Taco Rebels Fecha 1 Torneo 1 Temporada Bistec
POINTS_PER_BATTLE = 1 # Extra point per battle played

def loadFile(file_name: str):
    with Path(file_name).open('r', encoding="utf-8") as f:
        file = json.load(f)

    return file

def getScoresByBlader(matches, participants):
    scores = {}
    #Get the points scored by id
    for match in matches:
        match = match["attributes"] # Make shorter the dict
        player = match["points_by_participant"] # Make it more readable

        # Get the values using the json syntax
        id = match["identifier"]
        p1_id = player[0]["participant_id"]
        p1_score = player[0]["scores"][0]
        p2_id = player[1]["participant_id"]
        p2_score = player[1]["scores"][0]

        # The get() funciton returns the value if the key exists or the 2nd parameter if it does not exist
        scores[p1_id] = scores.get(p1_id, 0) + p1_score + POINTS_PER_BATTLE
        scores[p2_id] = scores.get(p2_id, 0) + p2_score + POINTS_PER_BATTLE

    #substitute id by a name
    for blader in participants:
        # The keyword starts with a blank space to avoid doing extra operations to look for it and remove it
        invitation_keyword = " (invitation pending)"
        name = blader["attributes"]["name"].lower().replace(invitation_keyword, "")
        id = int(blader["id"])

        #Renaming the key; pop method removes the old key and returns the value assigned
        scores[name] = scores.pop(id)
        print(name, "\t", scores[name])

    return scores

def assignPointsScored(scores, bladers):
    points = {}

    for blader in bladers:
        for name in blader["names"]:
            if name in scores:
                blader[SCORE_KEY] = blader[SCORE_KEY] + scores[name]
                break # Avoid using the remaining names
            else:
                print(name, "no existe")

    return bladers

def saveScores(scores: dict, filename: str) -> None:
    bladers = {"bladers": scores}
    with Path(filename).open('w', encoding="utf-8") as f:
        json.dump(bladers, f, indent=4, ensure_ascii=False)


def main():
    bladers = loadFile(FILE_BLADERS)["bladers"]
    matches  = loadFile(FILE_RESULTS)["data"]
    participants = loadFile(FILE_RESULTS)["included"]

    scores_by_blader = getScoresByBlader(matches, participants)
    bladers = assignPointsScored(scores_by_blader, bladers)

    saveScores(bladers, FILE_BLADERS)

if(__name__ == "__main__"):
    main()