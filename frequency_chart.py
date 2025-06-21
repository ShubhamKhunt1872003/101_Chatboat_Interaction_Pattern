import pandas as pd

# Load the Excel sheet
file_path = "WES 101 - Insights into the Use of Patterns in Chatbot Interfaces.xlsx"
df = pd.read_excel(file_path, sheet_name="Codebook Khunt", header=1)

# Define chatbot category column ranges
customer_support_cols = df.columns[2:40]   # C to AN
government_cols = df.columns[39:65]        # AM to BM
darkpattern_cols = df.columns[66:]         # BO to EB

# Convert all values to lowercase for case-insensitive comparison
df = df.applymap(lambda x: x.lower() if isinstance(x, str) else x)

# Define pattern detection logic with case-insensitive comparisons
pattern_definitions = {
    "Access Level Landing Page": lambda x: x == "landing page",
    "Access Level Sub-page": lambda x: x == "sub-page",
    "Language German": lambda x: x == "german",
    "Language English": lambda x: x == "english",
    "Language Multilingual": lambda x: x == "multilingual",
    "Avtar LOGO": lambda x: x == "logo",
    "Avtar Human": lambda x: x == "human",
    "Avtar Chat Message": lambda x: x == "chat message",
    "Avtar Other or No": lambda x: x in ["other", "no"],
    "Gender Male": lambda x: x == "male",
    "Gender Female": lambda x: x == "female",
    "Gender Neutral": lambda x: x == "neutral",
    "Gender None or Unclear": lambda x: x in ["none", "unclear"],
    
    # Access Icon
    "Access Icon bottom right": lambda x: x == "bottom right",
    "Access Icon bottom left": lambda x: x == "bottom left",
    "Access Icon middle of the page": lambda x: x == "middle of the page",
    "Access Icon available by menu": lambda x: x == "available by menu",
    "Access Icon other": lambda x: x == "other",
    
    # Required Contact
    "Required Contact Req  uired": lambda x: x == "required",
    "Required Contact Voluntary": lambda x: x == "voluntary",
    "Required Contact Login": lambda x: x == "login",
    "Required Contact Other": lambda x: x == "other",
    "Required Contact No": lambda x: x == "no",
    
    # Text Input Field
    "Text Input Field Send Button Partially enabled": lambda x: x in ["send button", "partially enabled"],
    "Text Input Field Send Button Always Available": lambda x: x in ["send button", "always available"],
    "Text Input Field Other or No": lambda x: x in ["other", "no"],
    
    # Quick Replies
    "Quick Replies Round Under Message": lambda x: x in ["round", "under message"],
    "Quick Replies Round Above text input": lambda x: x in ["round", "above text input"],
    "Quick Replies Angular Under Message": lambda x: x in ["angular", "under message"],
    "Quick Replies Angular Above text input": lambda x: x in ["angular", "above text input"],
    "Quick Replies Other or No": lambda x: x in ["other", "no"],
    
    # Only Quick Replies
    "Only Quick Replies": lambda x: x == "yes",
    "No Only Quick Replies": lambda x: x == "no",
    
    # Voice input
    "Voice Input": lambda x: x == "yes",
    "No Voice Input": lambda x: x == "no",
    
    # Form Input
    "Form Input": lambda x: x == "yes",
    "No Form Input": lambda x: x == "no",
    
    # Chat Messages
    "Chat Message Bubbles Attached two different sides": lambda x: x in ["bubbles", "attached two different sides"],
    "Chat Message Angular Attached two different sides": lambda x: x in ["angular", "attached two different sides"],
    "Chat Message No or Other": lambda x: x in ["no", "other"],
    
    # Cards
    "Card Only picture": lambda x: x == "only picture", 
    "Card several button": lambda x: x == "several buttons", 
    "Card One button": lambda x: x == "one button",
    "Card Other or No": lambda x: x in ["other", "no"],
    
    # Carousel
    "Carousel Scrollable": lambda x: x == "scrollable",
    "Carousel Arrow Control": lambda x: x == "arrow control",
    "Carousel Other or Not": lambda x: x in ["other", "not"],
    
    # Webview
    "Webview Product": lambda x: x == "product",
    "Webview Other Application": lambda x: x == "other application",
    "Webview Other or Not": lambda x: x in ["other", "no"],
    
    # Accordion
    "Accordion For chat messages": lambda x: x == "for chat messages",
    "Accordion For Quick Replay": lambda x: x == "for quick replay",
    "Accordion For Search Result": lambda x: x == "for search result",
    "Accordion Other or No": lambda x: x in ["other", "no"],
    
    # Transcript download
    "Transcript download via mail": lambda x: x == "via mail",
    "Transcript download Download": lambda x: x == "download",
    "Transcript download Other or No": lambda x: x in ["other", "no"],
    
    # System Information
    "System Information Top of the interface": lambda x: x == "top of the interface",
    "System Information bottom of the interface": lambda x: x == "bottom of the interface",
    "System Information before conversation": lambda x: x == "before conversation",
    "System Information after conversation": lambda x: x == "after conversation",
    "System Information in conversation": lambda x: x == "in conversation",
    "System Information data privacy": lambda x: x == "data privacy",
    "System Information platform provider": lambda x: x == "platform provider",
    "System Information Other or No": lambda x: x in ["other", "no"],
    
    # Information System
    "Information System": lambda x: x == "yes",
    "No Information System": lambda x: x == "no",
    
    # Name Stamps
    "Name Stamps Top of the interface": lambda x: x == "top of the interface",
    "Name Stamps bottom of the interface": lambda x: x == "bottom of the interface",
    "Name Stamps above message": lambda x: x == "above message",
    "Name Stamps under message": lambda x: x == "under message",
    "Name Stamps include user name": lambda x: x == "include user name",
    "Name Stamps for chatbot": lambda x: x == "for chatbot",
    "Name Stamps for user": lambda x: x == "for user",
    "Name Stamps Other or No": lambda x: x in ["other", "no"],
    
    # Date Stamps
    "Date Stamps Top of the interface": lambda x: x == "top of the interface",
    "Date Stamps bottom of the interface": lambda x: x == "bottom of the interface",
    "Date Stamps above message": lambda x: x == "above message",
    "Date Stamps under message": lambda x: x == "under message",
    "Date Stamps Other or No": lambda x: x in ["other", "no"],
    
    # Time Stamp
    "Time Stamp at the top of the conversation": lambda x: x == "at the top of the conversation",
    "Time Stamp bottom of the interface": lambda x: x == "bottom of the interface",
    "Time Stamp above message": lambda x: x == "above message",
    "Time Stamp under message": lambda x: x == "under message",
    "Time Stamp Other or No": lambda x: x in ["other", "no"],
    
    # Typing indicator
    "Typing indicator Three Dots": lambda x: x == "three dots",
    "Typing indicator X is typing": lambda x: x == "x is typing",
    "Typing indicator Animates Symbol": lambda x: x == "animates symbol",
    "Typing indicator Thinking": lambda x: x == "thinking",
    "Typing indicator Other or No": lambda x: x in ["other", "no"],
    
    # Notification
    "Notification Unread messages": lambda x: x == "unread messages",
    "Notification Popup": lambda x: x == "popups",
    "Notification Other or no": lambda x: x in ["other", "no"],
    
    # Audio Notification
    "Audio Notification": lambda x: x == "yes",
    "No Audio Notification": lambda x: x == "no",
    
    # Permanent Menu
    "Permanent Menu Burger Menu": lambda x: x in ["burger menu"],
    "Permanent Menu Meatball Menu": lambda x: x in ["meatball menu"],
    "Permanent Menu Kabab Menu": lambda x: x in ["kabab menu"],
    "Permanent Menu Plus sign": lambda x: x in ["plus sign"],
    "Permanent Menu in Header": lambda x: x in ["in header"],
    "Permanent Menu in Footer": lambda x: x in ["in footer"],
    "Permanent Menu Other or No": lambda x: x in ["other", "no"],
    
    # Action Icons
    "Action Icons Transcript download": lambda x: x in ["transcript download"],
    "Action Icons Dialog Replay": lambda x: x in ["dialog replay"],
    "Action Icons Font Size": lambda x: x in ["font size"],
    "Action Icons Notification options": lambda x: x in ["notification options"],
    "Action Icons Attachment": lambda x: x in ["attachment"],
    "Action Icons Emoji": lambda x: x in ["emoji"],
    "Action Icons Other or No": lambda x: x in ["other", "no"],
    
    # Call-on menu
    "Call-on menu chat messages": lambda x: x == "chat messages",
    "Call-on menu quick replies": lambda x: x == "quick replies",
    "Call-on menu other or no": lambda x: x in ["other", "not"],
    
    # Conversation Recovery
    "Conversation Recovery chat messages": lambda x: x == "chat messages",
    "Conversation Recovery quick replies": lambda x: x == "quick replies",
    "Conversation Recovery other or no": lambda x: x in ["other", "not"],
    
    # Dialog Replay
    "Dialog Replay": lambda x: x == "yes",
    "No Dialog Replay": lambda x: x == "no",
    
    # Live Agent contact
    "Live Agent": lambda x: x == "yes",
    "No Live Agent": lambda x: x == "no",
    
    # Functionality Introduction
    "Functionality Introduction Funcationality overview": lambda x: x == "funcationality overview",
    "Functionality Introduction Only Welcome Message": lambda x: x == "only welcome message",
    "Functionality Introduction Quick Reply": lambda x: x == "quick reply",
    "Functionality Introduction Other or No": lambda x: x in ["other", "no"],
    
    # FAQs
    "FAQs In chat": lambda x: x == "in chat",
    "FAQs In permanent menu": lambda x: x == "in permanent menu",
    "FAQs Other or No": lambda x: x in ["other", "no"],
    
    # Feedback Form
    "Feedback Form On message": lambda x: x == "on message",
    "Feedback Form on Chatbot": lambda x: x == "on chatbot",
    "Feedback Form Other or No": lambda x: x in ["other", "no"],
    
    # Message Reactions
    "Message Reactions Thumbs up/down": lambda x: x == "thumbs up/down",
    "Message Reactions Stars": lambda x: x == "stars",
    "Message Reactions Other or No": lambda x: x in ["other", "no"],
}

# Create a list to store results in order
results = []

# Count patterns for each category in the defined order
for pattern_name in pattern_definitions.keys():
    pattern_data = {"Pattern Name": pattern_name}
    condition = pattern_definitions[pattern_name]
    
    # Initialize counts
    cs_count = 0
    gov_count = 0
    dp_count = 0
    
    # Count for Customer Support (each chatbot counts only once per pattern)
    for col in customer_support_cols:
        unique_values = set(df[col].dropna())
        if any(condition(val) for val in unique_values):
            cs_count += 1
    
    # Count for Government (each chatbot counts only once per pattern)
    for col in government_cols:
        if df[col].apply(condition).any():
            gov_count += 1
    
    # Count for Darkpattern (each chatbot counts only once per pattern)
    for col in darkpattern_cols:
        if df[col].apply(condition).any():
            dp_count += 1
    
    pattern_data["Customer Support"] = cs_count
    pattern_data["Government"] = gov_count
    pattern_data["Darkpattern"] = dp_count
    pattern_data["Total"] = cs_count + gov_count + dp_count
    
    results.append(pattern_data)

# Convert to DataFrame
result_df = pd.DataFrame(results)

# Save to CSV
output_csv_path = "chatbot_pattern_frequency_table.csv"
result_df.to_csv(output_csv_path, index=False)
print(f"✅ Corrected frequency table saved to: {output_csv_path}")
print("Note: Each chatbot is counted only once per pattern, regardless of how many cells match")