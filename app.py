import os 
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

# SIDEBAR MENU
st.sidebar.title("Navigasi")
menu = st.sidebar.selectbox(
    "Pilih Menu",
    [
        "Upload Data",
        "Tampilkan Data",
        "Grafik Churn",
        "EDA",
        "Modeling",
        "Prediction",
        "Business Insights"
    ]
)

# 1. MENU UPLOAD DATA
default_file = "data/churn.csv"

if "df" not in st.session_state:
    if os.path.exists(default_file):
        st.session_state.df = pd.read_csv(default_file)

# 2. MENU TAMPILKAN DATA
elif menu == "Tampilkan Data":
    st.header("📊 Dataset Churn")

    if "df" not in st.session_state:
        st.warning("Silakan upload data terlebih dahulu.")
    else:
        df = st.session_state.df
        st.dataframe(df)

        # ICON CARDS
        col1, col2, col3, col4, col5 = st.columns(5)

        with col1:
            st.metric("📌 Total Customer", len(df))

        with col2:
            if "Churn" in df.columns:
                st.metric("👥 Total Churn", df["Churn"].value_counts().get("Yes", 0))

        with col3:
            if "Churn" in df.columns:
                churn_rate = df["Churn"].value_counts().get("Yes", 0) / len(df) * 100
                st.metric("💡 Churn Rate (%)", f"{churn_rate:.2f}%")

        with col4:
            if "PhoneService" in df.columns:
                st.metric("📞 Phone Service", df["PhoneService"].value_counts().get("Yes", 0))

        with col5:
            if "InternetService" in df.columns:
                st.metric("📶 Fiber Optic Users", df["InternetService"].value_counts().get("Fiber optic", 0))

        st.subheader("📌 Dataframe")
        st.dataframe(df)

        with st.expander("📊 Statistik Deskriptif"):
            st.write(df.describe())

        with st.expander("📁 Info Kolom"):
            info = pd.DataFrame({
                "dtype": df.dtypes.astype(str),
                "n_unique": df.nunique()
            })
            st.dataframe(info)

# 3. MENU GRAFIK CHURN
elif menu == "Grafik Churn":
    st.header("📊 Visualisasi Churn")

    if "df" not in st.session_state:
        st.warning("Silakan upload data terlebih dahulu.")
    else:
        df = st.session_state.df

        if "Churn" not in df.columns:
            st.error("Dataset tidak memiliki kolom 'Churn'.")
        else:
            churn_counts = df["Churn"].value_counts()

            # Bar chart
            st.subheader("🔹 Perbandingan Pelanggan Churn")
            fig1, ax1 = plt.subplots()
            ax1.bar(churn_counts.index, churn_counts.values)
            st.pyplot(fig1)

            # Pie chart
            st.subheader("🔹 Persentase Churn")
            fig2, ax2 = plt.subplots()
            ax2.pie(churn_counts.values, labels=churn_counts.index, autopct="%1.1f%%")
            st.pyplot(fig2)


# 4. MENU EDA
elif menu == "EDA":
    st.header("🔍 Exploratory Data Analysis")

    if "df" not in st.session_state:
        st.warning("Silakan upload data terlebih dahulu.")
    else:
        df = st.session_state.df

        numeric_cols = df.select_dtypes(include="number").columns

        if len(numeric_cols) == 0:
            st.error("Tidak ada kolom numerik untuk dianalisis.")
        else:
            col_choice = st.selectbox("Pilih kolom numerik", numeric_cols)

            fig, ax = plt.subplots()
            ax.hist(df[col_choice], bins=30)
            ax.set_title(f"Distribusi {col_choice}")
            st.pyplot(fig)


# 5. MENU MODELING
elif menu == "Modeling":
    st.header("🤖 Modeling Churn")

    if "df" not in st.session_state:
        st.warning("Silakan upload data terlebih dahulu.")
    else:
        df = st.session_state.df

        if "Churn" not in df.columns:
            st.error("Dataset memerlukan kolom 'Churn' untuk modeling.")
            st.stop()

        df_model = df.copy()
        df_model["Churn"] = df_model["Churn"].map({"Yes": 1, "No": 0})

        # Fitur numerik otomatis
        numeric_cols = df_model.select_dtypes(include="number").columns.drop("Churn")

        if len(numeric_cols) == 0:
            st.error("Tidak ada fitur numerik untuk modeling.")
            st.stop()

        X = df_model[numeric_cols].fillna(0)
        y = df_model["Churn"]

        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=0.2, random_state=42
        )

        model = LogisticRegression(max_iter=500)
        model.fit(X_train, y_train)

        y_pred = model.predict(X_test)

        st.write("### Akurasi:", accuracy_score(y_test, y_pred))
        st.write("### Confusion Matrix:")
        st.write(confusion_matrix(y_test, y_pred))
        st.write("### Classification Report:")
        st.text(classification_report(y_test, y_pred))

# 6. MENU PREDICTION
elif menu == "Prediction":
    st.header("🧮 Prediksi Churn Pelanggan Baru")

    if "df" not in st.session_state:
        st.warning("Silakan upload data terlebih dahulu.")
    else:
        df = st.session_state.df.copy()

        df["Churn"] = df["Churn"].map({"Yes": 1, "No": 0})
        numeric_cols = df.select_dtypes(include="number").columns.drop("Churn")

        st.write("Masukkan nilai untuk fitur berikut:")

        inputs = []
        for col in numeric_cols:
            value = st.number_input(col, float(df[col].min()), float(df[col].max()))
            inputs.append(value)

        if st.button("Prediksi"):
            model = LogisticRegression(max_iter=500)
            X = df[numeric_cols].fillna(0)
            y = df["Churn"]
            model.fit(X, y)

            pred = model.predict([inputs])[0]

            if pred == 1:
                st.error("⚠️ Pelanggan berpotensi CHURN!")
            else:
                st.success("✓ Pelanggan aman (tidak churn)")

# 7. MENU BUSINESS INSIGHTS
elif menu == "Business Insights":
    st.header("💼 Business Insights")
    st.write("""
    **🔍 Temuan Utama dari Customer Churn Analysis:**
    - Pelanggan dengan kontrak *month-to-month* paling banyak churn.
    - Harga bulanan lebih tinggi meningkatkan risiko churn.
    - Internet Fiber Optic memiliki tingkat churn tertinggi.
    - Pelanggan dengan tenure rendah cenderung churn lebih cepat.
    - Strategi retensi perlu diarahkan pada pelanggan baru dan pengguna fiber optic.
    """)
