# MACHINE-LEARNING-MODEL-IMPLEMENTATION
COMPANY : CODTECH IT SOLUTIONS

NAME : LIKHITHA N

INTERN ID : CT06DL625

DOMAIN : PYTHON PROGRAMMING

DURATION : 6 WEEKS

MENTOR : NEELA SANTOSH

DESCRIPTION:

# 📩 Spam Detector & 🇮🇳 Indian Holiday Checker using Streamlit

## 🔍 Project Overview

This project is part of the **CODTECH Internship Task 4**, where I developed a **machine learning-powered SMS Spam Detection system** integrated with a **Holiday Checker for India** using **Streamlit**. The application is interactive, visually intuitive, and allows users to classify SMS messages as **Spam or Not Spam** and verify whether a specific date is a **public holiday or weekend in India**.

The key goal of this task was to demonstrate the real-world application of machine learning and API integration through a deployable Python app. The app uses a trained **Naive Bayes classifier**, real-time **public holiday API** (`https://date.nager.at`), and built-in calendar logic to enhance user experience. This multi-functional tool showcases the ability to combine **NLP**, **data APIs**, and **web interface design** in a single deployable project.

---

## 🧠 Project Features

* ✅ **SMS Spam Classification** using a trained ML model.
* 📅 **Real-time Indian Public Holiday Checker** using external API.
* 🗓️ **Fallback Mechanism** using pre-downloaded JSON data in case of API issues.
* 📆 **Weekend Detection**: Identifies if a selected date is Saturday or Sunday.
* 🧪 Preloaded examples to test spam detection.
* 📂 Local saving of API data to `holidays.json`.
* 🎨 Styled and user-friendly interface using **Streamlit CSS** injection.
* 🔒 Graceful error handling and fallback for API failures.

---

## 📌 Task Description

The task was divided into two primary modules:

### 1. **SMS Spam Detection**

This module allows the user to input an SMS-like message, and the system predicts whether it is **spam or not spam** using a **Multinomial Naive Bayes** model. The model was trained on the **SMS Spam Collection Dataset** (downloaded from Kaggle), which contains thousands of labeled SMS messages. The input is preprocessed and vectorized using a **TF-IDF vectorizer**.

Users can:

* Type or paste a message into a text box.
* Click "Predict" to classify the message.
* View confidence percentage of prediction.
* Try sample spam messages provided in the UI.

### 2. **Indian Holiday Checker**

This module checks whether a given date (defaults to today) is a public holiday in India. It fetches real-time holiday data using the **Nager.Date API** and stores it locally as `holidays.json`.

If the API is down (204 No Content or other issues), the app:

* Loads fallback data from the saved file.
* Also identifies if the selected date is a **Saturday or Sunday**, showing it as a weekend.

The user can:

* Select any date from a calendar input.
* Check if it is a holiday or weekend.
* View upcoming fallback holidays if the API fails.

---

## 🛠️ Tools and Technologies Used

| Tool/Library     | Purpose                                         |
| ---------------- | ----------------------------------------------- |
| **Python 3.10+** | Core programming language                       |
| **Streamlit**    | Web app interface and layout                    |
| **Scikit-learn** | Model training and classification (Naive Bayes) |
| **Pandas**       | Data preprocessing and CSV parsing              |
| **Pickle**       | Model and vectorizer serialization              |
| **Requests**     | HTTP API calls to fetch holiday data            |
| **Datetime**     | Handling current and selected date values       |
| **JSON**         | Saving fallback holiday data                    |

---

## 💻 Platform and Environment

* **Code Editor:** Visual Studio Code (VS Code)
* **Operating System:** Windows 11
* **Python IDE:** Streamlit CLI via Terminal (`streamlit run app.py`)
* **Folder Structure:**

  ```
  /machine_learning/
  ├── app.py               # Main Streamlit app
  ├── holidays.json        # Fallback holiday data
  ├── spam.csv             # SMS spam dataset
  ├── train_model.py       # Training script for ML model
  ├── spam_model.pkl       # Trained spam detection model
  ├── vectorizer.pkl       # TF-IDF vectorizer
  ```

---

## 🌐 API Used

* **Nager.Date API**

  * Endpoint: `https://date.nager.at/api/v3/PublicHolidays/{year}/IN`
  * Returns official Indian public holidays in a given year.
  * Data is parsed and saved as a JSON fallback for offline use.

---

## 🧪 How it Works

1. **Spam Classifier:**

   * Loads `spam_model.pkl` and `vectorizer.pkl`.
   * Vectorizes user input.
   * Classifies with Naive Bayes.
   * Displays result with confidence level.

2. **Holiday Checker:**

   * Tries to fetch current year holidays from Nager API.
   * If unsuccessful, uses `holidays.json`.
   * Matches selected date with holiday list.
   * Also checks if the date is a **Saturday or Sunday**.

---

## 🌍 Applications

* 📱 **Telecom Providers:** Auto-filtering of spam SMS in real-time.
* 📅 **Event Planners:** Check public holidays to avoid scheduling clashes.
* 📈 **HR Management Systems:** Integration for automatic leave calendars.
* 🔒 **Security Apps:** Early spam/phishing detection based on message patterns.
* 📚 **Educational Projects:** Demonstrates full-stack machine learning in action.

---

## 🚀 Future Enhancements

* Add support for detecting **phishing** and **fraudulent links** in SMS.
* Schedule automatic updates for `holidays.json` weekly/monthly.
* Allow uploading bulk SMS to classify multiple entries at once.
* Deploy using **Streamlit Community Cloud**, **Render**, or **Heroku**.
* Add **search/filter** in the holiday list for better UX.

---

## 🙌 Final Thoughts

This project was both a learning and practical experience. It combines core machine learning principles, data APIs, and frontend deployment with **Streamlit**. From data preprocessing to model training and final deployment, it’s a complete end-to-end pipeline demonstrating **real-world machine learning** and Python development skills. The fallback handling, user interface, and model integration make it robust and useful in various domains.

OUTPUT
![Image](https://github.com/user-attachments/assets/7d4d9067-fee0-45df-bd72-7fd7dba79ead)

![Image](https://github.com/user-attachments/assets/64236851-2999-4be1-9dc9-cde57186af16)

![Image](https://github.com/user-attachments/assets/4e70fd10-5fa4-4c4e-9b9b-cac85f46abd2)

![Image](https://github.com/user-attachments/assets/57f3552f-9c43-4650-8ce9-c2f085cd3564)

![Image](https://github.com/user-attachments/assets/293e7c67-c2e5-425f-8178-e06d72cc5b97)

![Image](https://github.com/user-attachments/assets/ca2d78b3-ae2c-4a21-a43f-f95fdd91ce4e)

![Image](https://github.com/user-attachments/assets/dd15a59f-0611-4de0-8ea9-ff995d77621b)

![Image](https://github.com/user-attachments/assets/e4e9d2dc-91d1-4925-9879-8f4162411eb2)

![Image](https://github.com/user-attachments/assets/d856fa44-3fc8-4ac8-8168-90e20b1fd1cd)

![Image](https://github.com/user-attachments/assets/2382b1b2-5f34-47db-ad4a-f5c857a1b719)


