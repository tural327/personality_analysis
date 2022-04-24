from flask import Flask, render_template, request
import numpy as np
import pandas as pd
import pickle
import pandas as pd

loaded_model = pickle.load(open("model.sav", 'rb'))
app = Flask(__name__)


@app.route("/", methods=["POST", "GET"])
def test():
    my_end_res = ""
    my_list = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    if request.method == "POST" and "education" in request.form and "marrige" in request.form and "kidhome" in request.form and "teenhome" in request.form and "AcceptedCmp3" in request.form and "AcceptedCmp4" in request.form and "AcceptedCmp5" in request.form and "AcceptedCmp1" in request.form and "Response" in request.form and "income" in request.form and "Recency" in request.form and "MntFruits" in request.form and "MntMeatProducts" in request.form and "MntMeatProducts" in request.form and "NumWebPurchases" in request.form and "NumCatalogPurchases" in request.form and "NumStorePurchases" in request.form and "NumWebVisitsMonth" in request.form and "Income2" in request.form and "MntWines2" in request.form and "MntMeatProducts2" in request.form and "MntFishProducts2" in request.form and "MntGoldProds2" in request.form and "MntSweetProducts2" in request.form and "AcceptedCmp2" in request.form:
        ed = [0]
        ma = [0]
        kid = [0]
        teen = [0]
        Accep3 = [0]
        Accep4 = [0]
        Accep5 = [0]
        Accep1 = [0]
        Accep2 = [0]
        Res = [0]
        if request.form.get("education") == "Graduation":
            ed[0] = 0
        elif request.form.get("education") == "PhD":
            ed[0] = 1
        elif request.form.get("education") == "Basic":
            ed[0] = 2
        elif request.form.get("education") == "Master":
            ed[0] = 3
        elif request.form.get("education") == "2n Cycle":
            ed[0] = 4

        if request.form.get("marrige") == "Single":
            ma[0] = 0
        elif request.form.get("marrige") == "Together":
            ma[0] = 1
        elif request.form.get("marrige") == "Married":
            ma[0] = 2
        elif request.form.get("marrige") == "Divorced":
            ma[0] = 3
        elif request.form.get("marrige") == "Widow":
            ma[0] = 5
        elif request.form.get("marrige") == "YOLO":
            ma[0] = 8
        if request.form.get("kidhome") == "0":
            kid[0] = 0
        elif request.form.get("kidhome") == "1":
            kid[0] = 1
        elif request.form.get("kidhome") == "2":
            kid[0] = 2
        if request.form.get("teenhome") == "0":
            teen[0] = 0
        elif request.form.get("teenhome") == "1":
            teen[0] = 1
        elif request.form.get("teenhome") == "2":
            teen[0] = 2
        if request.form.get("AcceptedCmp3") == "0":
            Accep3[0] = 0
        elif request.form.get("AcceptedCmp3") == "1":
            Accep3[0] = 1
        if request.form.get("AcceptedCmp4") == "0":
            Accep4[0] = 0
        elif request.form.get("AcceptedCmp4") == "1":
            Accep4[0] = 1
        if request.form.get("AcceptedCmp5") == "0":
            Accep5[0] = 0
        elif request.form.get("AcceptedCmp5") == "1":
            Accep5[0] = 1
        if request.form.get("AcceptedCmp2") == "0":
            Accep2[0] = 0
        elif request.form.get("AcceptedCmp2") == "1":
            Accep2[0] = 1
        if request.form.get("AcceptedCmp1") == "0":
            Accep1[0] = 0
        elif request.form.get("AcceptedCmp1") == "1":
            Accep1[0] = 1
        if request.form.get("Response") == "0":
            Res[0] = 0
        elif request.form.get("Response") == "1":
            Res[0] = 1

        income = float(request.form.get("income"))
        Recency = float(request.form.get("Recency"))
        MntFruits = float(request.form.get("MntFruits"))
        MntMeatProducts = float(request.form.get("MntMeatProducts"))
        NumDealsPurchases = float(request.form.get("NumDealsPurchases"))
        NumWebPurchases = float(request.form.get("NumWebPurchases"))
        NumCatalogPurchases = float(request.form.get("NumCatalogPurchases"))
        NumStorePurchases = float(request.form.get("NumStorePurchases"))
        NumWebVisitsMonth = float(request.form.get("NumWebVisitsMonth"))
        Income2 = float(request.form.get("Income2"))
        MntWines2 = float(request.form.get("MntWines2"))
        MntMeatProducts2 = float(request.form.get("MntMeatProducts2"))
        MntFishProducts2 = float(request.form.get("MntFishProducts2"))
        MntGoldProds2 = float(request.form.get("MntGoldProds2"))
        MntSweetProducts2 = float(request.form.get("MntSweetProducts2"))

        my_list = [ed[0], ma[0], income, kid[0], teen[0], Recency, MntFruits, MntMeatProducts, NumDealsPurchases,
                   NumWebPurchases, NumCatalogPurchases, NumStorePurchases, NumWebVisitsMonth, Accep3[0], Accep4[0],
                   Accep5[0], Accep1[0], Accep2[0], 3, 11, Res[0], Income2, MntWines2, MntMeatProducts2,
                   MntFishProducts2, MntGoldProds2, MntSweetProducts2]


        a = pd.DataFrame(my_list)
        m = a.T
        res_list = loaded_model.predict(m)
        end_res = str(res_list[0])
        my_end_res = end_res

    return render_template("index.html" , my_end_res = my_end_res)


if __name__ == "__main__":
    app.run()