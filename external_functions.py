import csv
import os
import re




def get_audio_profiles():
    """Returns a dictionary of dictionaries of the audio profiles defined in audio_profiles.csv"""
    audio_profiles = {}
    with open('audio_profiles.csv') as csv_file:
        csv_reader = csv.DictReader(csv_file, delimiter=',')
        for row in csv_reader:
            person = row["person"]
            language_code = row ["language_code"]
            name = row["name"]
            try:
                pitch = float(row["pitch"])
            except:
                continue
            audio_profiles[person] = {"language_code": language_code, "name": name, "pitch": pitch}
    return audio_profiles





def get_day_num(specified_court_date, transcripts):
    """Returns the day number for the specified court date. For example,\n
    get_day_num("2005-02-28") = 1"""
    for n, court_date in enumerate(transcripts.keys()):
        if court_date == specified_court_date:
            return n + 1




def get_part_character_count(transcript, segment_num):
    """Returns the number of characters of the current part in the transcript, as delimited by recesses.\n
    If the text of the specified segment number contains "Recess taken.", the character count refers to\n
    the part before that segment."""

    char_count = 0
    num_segments = len(transcript)

    # Character count for previous speaking segments in part. Does not change the value of char_count if there are no previous segments
    previous_segment_num =  segment_num - 1
    while previous_segment_num >= 0:
        speaking_segment = transcript[previous_segment_num]
        text = speaking_segment["text"]
        if re.search("Recess taken", text):
            break
        else:
            char_count += len(text)
            previous_segment_num -= 1
    
    # Character count for subsequent speaking segments in part. Does not change the value of char_count if there are no subsequent segments
    subsequent_segment_num =  segment_num
    while subsequent_segment_num < num_segments:
        speaking_segment = transcript[subsequent_segment_num]
        text = speaking_segment["text"]
        if re.search("Recess taken", text):
            break
        else:
            char_count += len(text)
            subsequent_segment_num += 1

    return char_count





def get_num_parts(transcript, min_characters_per_part):
    """Returns the total number of parts for the provided court date, as defined by the number of recess messages\n
    for which the character count is at least 20000"""
    part_count = 1
    part_word_count = 0
    for segment_num, speaking_segment in enumerate(transcript):
        text = speaking_segment["text"]
        speaker = speaking_segment["speaker"]
        part_word_count += len(text)
        if (speaker == "Recess Message" and 
            get_part_character_count(transcript, segment_num) >= min_characters_per_part and # current part
            get_part_character_count(transcript, segment_num+1) >= min_characters_per_part): # next part
            part_count += 1
            part_word_count = 0
    return part_count





def get_timestamps(court_date, segment_num, speaker):
    """Returns a list of timestamps for the location given by court_date, segment_num and speaker."""
    timestamp_file_path = os.path.join(
        court_date,
        "timestamps",
        str(segment_num).zfill(4) + "_" + re.sub("[\.',]+", "", speaker.lower().replace(" ", "_")) + ".txt")
    with open(timestamp_file_path, "r") as file:
        timestamps = [float(line.strip()) for line in file]
    return timestamps





formatted_pattern = re.compile("^(?P<speaker>[A-Za-z0-9 \.,'\(\)]+): (?P<text>[\S ]+)") # Pattern for extracting speaker and text from formatted transcripts
def retrieve_formatted_transcripts():
    all_dates2 = {}
    directory_path = "Formatted Transcripts"
    for file_name in os.listdir(directory_path):
        file_path = os.path.join(directory_path, file_name)
        court_date = []
        with open(file_path, encoding="utf-8") as file:
            for n, line in enumerate(file.readlines()):
                pattern_match = formatted_pattern.search(line)
                if not pattern_match:
                    print(line)
                    continue
                speaker = pattern_match.group("speaker")
                text = pattern_match.group("text")
                speaking_segment = {"speaker": speaker, "text": text}
                court_date.append(speaking_segment)
        date = "2005-" + file_name.split(".")[0] # Returns 2005-03-22 for 03-22.txt
        all_dates2[date] = court_date
    return all_dates2