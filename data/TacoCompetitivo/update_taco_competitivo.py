from pathlib import Path
import json

TOURNAMENT_TYPE = "R" #L=League, F=Fun, R=Rebels
DATE = "07" #Fecha
PART = "1" #1=single 2=double
SEASON = "B" #B=Bistec

SCORE_KEY = f"score_tc"
INVITATION_KEYWORD = " (invitation pending)"

FILE_BLADERS = "../bladers.json"
FILE_RESULTS = f"../TacoRebels/T{TOURNAMENT_TYPE}F{DATE}0{PART}{SEASON}.json" #TRF0101B means Taco Rebels Fecha 1 Torneo 1 Temporada Bistec
POINTS_PER_BATTLE = 0 # Extra point per battle played

def loadFile(file_name: str):
    with Path(file_name).open('r', encoding="utf-8") as f:
        file = json.load(f)

    return file

def isTaco(id, participants, bladers):
    is_taco = False
    blader_name = ""
    for participant in participants:
        if(participant["id"] == str(id)):
            blader_name = participant["attributes"]["name"].lower().replace(INVITATION_KEYWORD, "")
            break
    
    for blader in bladers:
        if(("is_taco" in blader) and (blader["is_taco"] == 1)):
            for name in blader["names"]:
                if(blader_name == name):
                    is_taco = True
                    break
    return(is_taco, blader_name)


def getScoresByBlader(matches, participants, bladers):
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

        is_taco1, blader_name1 = isTaco(p1_id, participants, bladers)
        is_taco2, blader_name2 = isTaco(p2_id, participants, bladers)

        if(is_taco1 and is_taco2):
            print("Batalla de Tacos", blader_name1, "vs", blader_name2, "=", p1_score, "-", p2_score)
            if(p1_score > p2_score):
                scores[blader_name1] = scores.get(blader_name1, 0) + 1
                scores[blader_name2] = scores.get(blader_name2, 0) - 1
            else:
                scores[blader_name1] = scores.get(blader_name1, 0) - 1
                scores[blader_name2] = scores.get(blader_name2, 0) + 1

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

def printSortedScores(scores):
    sorted_scores = {k: v for k, v in sorted(scores.items(), key=lambda item: item[1], reverse=True)}
    pos = 0
    count = 0
    value = 256 #A big value to start the comparation
    for name in sorted_scores:
        if(value != sorted_scores[name]):
            pos = count+1
            value = sorted_scores[name]
        count = count+1
        print(pos, "\t", name, "\t", sorted_scores[name])

def main():
    bladers = loadFile(FILE_BLADERS)["bladers"]
    matches  = loadFile(FILE_RESULTS)["data"]
    participants = loadFile(FILE_RESULTS)["included"]

    scores_by_blader = getScoresByBlader(matches, participants, bladers)
    bladers = assignPointsScored(scores_by_blader, bladers)

    saveScores(bladers, FILE_BLADERS)
    printSortedScores(scores_by_blader)

if(__name__ == "__main__"):
    main()