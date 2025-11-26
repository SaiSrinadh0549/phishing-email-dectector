# train_phishing.py
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
from sklearn.metrics import classification_report, accuracy_score
import joblib

# Small sample dataset (expanded demo: adds more varied examples)
data = [
    # phishing-like
    ("Your account has been compromised. Click here to reset your password: http://evil.example", 1),
    ("Please verify your account immediately by clicking the link below to avoid suspension", 1),
    ("Urgent: Your mailbox is full. Update now to avoid suspension http://phish.example", 1),
    ("You received a secure message from Bank. Please sign in: http://bank.example", 1),
    ("We detected unusual login activity. Confirm your identity here: http://confirm.example", 1),
    ("Final notice: Your payment failed. Login to update billing: http://pay.example", 1),
    ("Congratulations! You won a prize. Claim now: http://scam.example", 1),
    ("Action required: Your password will expire today. Click to renew.", 1),

    # more subtle phishing (social engineering)
    ("Hi, this is IT. We need your credentials to upgrade the mail server. Reply with username/password", 1),
    ("Please review the attached invoice and click the secure link to download the statement", 1),

    # ham / safe examples
    ("Meeting notes for today's scrum attached. Let me know your thoughts.", 0),
    ("Invoice for your recent purchase attached. Thank you for shopping with us", 0),
    ("Lunch tomorrow? 1 PM works for me.", 0),
    ("Weekly report attached. Great job everyone!", 0),
    ("Hi team, here is the agenda for tomorrow's meeting. Please add items.", 0),
    ("Can you review the PR I opened? It fixes the bug in the auth flow.", 0),
    ("Reminder: The office will be closed Friday for the holiday.", 0),
    ("Here's the document with the Q4 metrics. Let me know if you'd like changes.", 0),

    # mixture to increase variety
    ("Support: your ticket 12345 has been updated. See details in your portal.", 0),
    ("Security alert: unknown device signed in to your account. If this wasn't you, reset password.", 1),
    ("Invitation: join our team meeting via the calendar link", 0),
    ("Your subscription will renew on 01/01/2026. No action required if you want to continue.", 0),
    ("Verify billing information now to avoid interruption: http://billing.example", 1),
    ("Attached are the slides for tomorrow's presentation. Feedback welcome.", 0),
]


# Put data into a DataFrame
df = pd.DataFrame(data, columns=["text", "label"])

# Split into train and test
X_train, X_test, y_train, y_test = train_test_split(
    df["text"],
    df["label"],
    test_size=0.25,
    random_state=42,
)

# Pipeline: TF-IDF + Logistic Regression
pipeline = Pipeline([
    ("tfidf", TfidfVectorizer(ngram_range=(1, 2), max_features=5000)),
    ("clf", LogisticRegression(max_iter=1000)),
])

# Train the model
pipeline.fit(X_train, y_train)

# Evaluate
preds = pipeline.predict(X_test)
print("Accuracy:", accuracy_score(y_test, preds))
print(classification_report(y_test, preds))

# Save model
joblib.dump(pipeline, "phishing_model.joblib")
print("Saved model to phishing_model.joblib")
