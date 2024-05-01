from util import write_csv

def process_video(video_path):
    # Your existing code for processing the video goes here

    # Save results to a CSV file
    write_csv(results, './test.csv')
    progress_label.config(text="Results saved to test.csv")
