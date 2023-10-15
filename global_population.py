{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyNQRc4Zgkn55DIyJs/2TZHk"
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "KBr8SIWNQXWi"
      },
      "outputs": [],
      "source": [
        "import pickle\n",
        "import streamlit as st\n",
        "import pandas as pd\n",
        "import matplotlib.pyplot as plt\n",
        "\n",
        "model = pickle.load(open('prediksi_populasi.sav','rb'))\n",
        "\n",
        "df = pd.read_csv('Global_annual_population.csv')\n",
        "df['Year'] = pd.to_datetime(df['Year'], format='%Y')\n",
        "df.set_index(['Year'], inplace=True)\n",
        "\n",
        "st.title('Forecasting Populasi')\n",
        "year = st.slider(\"Tentukan Tahun\",1,30, step=1)\n",
        "\n",
        "pred = model.forecast(year)\n",
        "pred = pd.DataFrame(pred, columns=['Population'])\n",
        "\n",
        "if st.button(\"Predict\"):\n",
        "\n",
        "    col1, col2 = st.columns([2,3])\n",
        "    with col1:\n",
        "        st.dataframe(pred)\n",
        "    with col2:\n",
        "        fig, ax = plt.subplots()\n",
        "        df['Population'].plot(style='--', color='gray', legend=True, label='known')\n",
        "        pred['Population'].plot(color='b', legend=True, label='Prediction')\n",
        "        st.pyplot(fig)"
      ]
    }
  ]
}