INPUT_FILE_PATH = "example.txt"

def getData(path):
    with open(INPUT_FILE_PATH, "r") as File:
        patterns = list()
        outputs = list()
        for line in File:
            parts = line.split()
            split = parts.index("|")
            patterns.append(list(parts[:split]))        # Patterns are all parts of input before delimiter.
            outputs.append(list(parts[split + 1:]))     # Outputs are all parts of input after delimiter.
    return patterns, outputs


def main():
    patterns, outputs = getData(INPUT_FILE_PATH)
    numberSegments = {  # Which segments make up each number.
        1: ("c", "f"), 
        2: ("a", "c", "d", "e", "g"), 
        3: ("a", "c", "d", "f", "g"), 
        4: ("b", "c", "d", "f"), 
        5: ("a", "b", "d", "f", "g"), 
        6: ("a", "b", "d", "e", "f", "g"), 
        7: ("a", "c", "f"), 
        8: ("a", "b", "c", "d", "e", "f", "g"), 
        9: ("a", "b", "c", "d", "f", "g"),
    }
    segmentsPerNumber = {number:len(segments) for (number, segments) in numberSegments.items()}    # How many segments are required for each number.
    

if __name__ == "__main__":
    main()
