import pandas as pd
import json
import os


class FewShotPosts:
    def __init__(self, file_path=os.path.join("data", "preprocessed.json")):
        self.df = None
        self.unique_tags = None
        self.load_posts(file_path)

    def load_posts(self, file_path):
        with open(file_path, encoding="utf-8") as f:
            posts = json.load(f)
            self.df = pd.json_normalize(posts)
            self.df['length'] = self.df['line_count'].apply(self.categorize_length)
            # collect unique tags (global)
            all_tags = self.df['tags'].apply(lambda x: x).sum()
            self.unique_tags = list(set(all_tags))

    def categorize_length(self, line_count):
        if line_count < 5:
            return "Short"
        elif 5 <= line_count <= 10:
            return "Medium"
        else:
            return "Long"

    # Filter by length + language + tag
    def get_filtered_posts(self, length, language, tag):
        df_filtered = self.df[
            (self.df['tags'].apply(lambda tags: tag in tags)) &
            (self.df['language'] == language) &
            (self.df['length'] == length)
        ]
        return df_filtered.to_dict(orient='records')

    # Get all tags per influencer
    def get_tags_per_influencer(self):
        influencer_tags = (
            self.df.groupby("influencer")["tags"]
            .apply(lambda x: set(tag for tags in x for tag in tags))
            .to_dict()
        )
        return influencer_tags

    # Get top posts by engagement
    def get_top_posts(self, top_n=5, min_engagement=0):
        df_top = self.df[self.df["engagement"] >= min_engagement]
        return df_top.nlargest(top_n, "engagement").to_dict(orient="records")

    # Filter posts by engagement level (Low / Medium / High)
    def get_posts_by_engagement(self, level="High"):
        if level == "Low":
            df_filtered = self.df[self.df["engagement"] <= 200]
        elif level == "Medium":
            df_filtered = self.df[(self.df["engagement"] > 200) & (self.df["engagement"] <= 500)]
        else:  # High
            df_filtered = self.df[self.df["engagement"] > 500]
        return df_filtered.to_dict(orient="records")

    def get_tags(self):
        return self.unique_tags


if __name__ == "__main__":
    fs = FewShotPosts()

    # Example usage
    print("Unique tags per influencer:")
    print(fs.get_tags_per_influencer())

    print("\nTop 3 posts with engagement >= 100:")
    print(fs.get_top_posts(top_n=3, min_engagement=50))

    print("\n High engagement posts:")
    print(fs.get_posts_by_engagement("High"))

        