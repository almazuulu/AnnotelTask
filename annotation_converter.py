import json

def convert(annotell_annotation):
    # Creating dictionary for elements in OpenLabel
    # creating lists to store the name of class and its ids
    shapePropertiesList = []
    classList = []
    for k, v in annotell_annotation['shapeProperties'].items():
        shapePropertiesList.append(k)
        for a, b in v.items():
            for c, d in b.items():
                if c != 'class':
                    continue
                classList.append(d)

    # storing from created lists to the dictionary of objects
    elements = {
        "objects":
            {

            }
    }
    # objects dictionary has been created:
    for i in range(len(shapePropertiesList)):
        elements["objects"][shapePropertiesList[i]] = {
            "name": shapePropertiesList[i],
            "type": classList[i]
        }

    rdfObjListId = []
    pushingOrPullingList = []
    relationsDict = {

    }

    for k, v in annotell_annotation["shapeProperties"].items():
        for a, b in v.items():
            if "ObjectType" not in b:
                continue
            if b["PushingOrPulling"] != "Nothing":
                rdfObjListId.append([k, b["PushingOrPulling"]["shape"]])
            else:
                rdfObjListId.append([k, b["PushingOrPulling"]])

    #################################################
    # Creating dictionary set for relationsDict in OpenLabel
    for i in range(len(rdfObjListId)):
        relationsDict[str(i)] = {
            "name": str(i),
            "rdf_objects": [
                {"type": "object",
                 "uid": rdfObjListId[i][0]
                 }
            ],
            "rdf_subjects":
                [
                    {
                        "type": "object",
                        "uid": rdfObjListId[i][1]
                    }
                ],
            "type": "PushingOrPulling"
        }

    #################################################
    # Creating dictionary set for frames in OpenLabel

    framesDict = {
        "": {
            "objects": {

            }
        }
    }

    shapeFeatures = annotell_annotation["shapes"]["CAM"]["features"]

    idNameList = list()
    coordinatesList = list()

    counter = 0

    maxCoordinatesXY = list()
    for i in range(len(shapeFeatures)):
        idNameList.append(shapeFeatures[counter]["id"])

        maxXCoordinate_0 = shapeFeatures[counter]["geometry"]["coordinates"]["maxX"]["coordinates"][0]
        maxYCoordinate_1 = shapeFeatures[counter]["geometry"]["coordinates"]["maxY"]["coordinates"][1]

        minXCoordinate_0 = shapeFeatures[counter]["geometry"]["coordinates"]["minX"]["coordinates"][0]
        minYCoordinate_1 = shapeFeatures[counter]["geometry"]["coordinates"]["minY"]["coordinates"][1]

        coordinate1 = (maxXCoordinate_0 + minXCoordinate_0) / 2
        coordinate2 = (maxYCoordinate_1 + minYCoordinate_1) / 2
        coordinate3 = (maxXCoordinate_0 - minXCoordinate_0)
        coordinate4 = (maxYCoordinate_1 - minYCoordinate_1)

        coordinatesList.append([coordinate1, coordinate2, coordinate3, coordinate4])
        counter += 1

    listCoordinates = [list(x) for x in zip(idNameList, coordinatesList)]

    rdfObjListId2 = []

    for k, v in annotell_annotation["shapeProperties"].items():
        for a, b in v.items():
            if "ObjectType" not in b:
                continue
            if b["PushingOrPulling"] != "Nothing":
                rdfObjListId2.append([k, b["PushingOrPulling"]["shape"], b["ObjectType"]])
            else:
                rdfObjListId2.append([k, b["PushingOrPulling"], b["ObjectType"]])

    for i in range(len(listCoordinates)):
        if listCoordinates[i][0] not in (rdfObjListId2[0][0], rdfObjListId2[1][0]):
            framesDict[""]["objects"].update({
                listCoordinates[i][0]: {
                    "object_data": {
                        "bbox": [
                            {
                                "name": "bbox_206bd",
                                "stream": "CAM",
                                "val":
                                    [i for i in listCoordinates[i][1]]
                            },

                        ],
                        "boolean": [
                            {
                                "name": "Unclear",
                                "val": True
                            }
                        ]
                    }
                }
            })
        elif listCoordinates[i][0] in (rdfObjListId2[0][0], rdfObjListId2[1][0]):
            framesDict[""]["objects"].update({
                listCoordinates[i][0]: {
                    "object_data": {
                        "bbox": [
                            {
                                "name": "bbox_206bd",
                                "stream": "CAM",
                                "val":
                                    [i for i in listCoordinates[i][1]]
                            },

                        ],
                        "boolean": [
                            {
                                "name": "Unclear",
                                "val": False
                            }
                        ],

                        "text": [
                            {
                                "name": "ObjectType",
                                "val": "Car"
                            }
                        ]
                    }
                }
            })

    framesDict[""]["relations"] = {
        "0": {},
        "1": {}
    }

    #################################################
    # Joining all together and creating converted Dataset for OpenLabel


    dataDictionary = {
        "data": {
            "openlabel":
                {
                    "objects": elements["objects"],
                    "relations": relationsDict,
                },
            "frames": framesDict
        }
    }

    return dataDictionary


def converting_to_json(annotell_annotation):
    with open("converted.json", "w") as outfile:
        json.dump(convert(annotell_annotation), outfile, indent=4)
        print('file created successfully!')
if __name__ == "__main__":
    pass
