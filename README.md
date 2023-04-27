# FAO_25042023
"Hungry in the World" - public health study

ISSUE :

    - What are the impacts of the prevalence of undernourishment and malnutrition on populations in the World ?

    - Will the Food and Agriculture Organization of the United Nations' (FAO) goals to eradicate hunger and malnutrition be reached by 2030?

INTRODUCTION :

THE GLOBAL HUNGER INDEX (GHI)
  The GHI results are based on a formula that combines three 
  dimensions of hunger - insufficient caloric intake, child undernutrition, and child mortality - measured by four indicators:
    > UNDERNOURISHMENT: the share of the population that is undernourished, reflecting 
    Undernourishment: the proportion of the population that is undernourished, reflecting inadequate caloric intake
    > INFANTILE EMACIATION: the proportion of children under 5 years of age who are 
  wasting (low weight for height), reflecting acute undernutrition 
  reflecting acute undernutrition 
    > Stunting: the proportion of children under 5 years of age who are stunted 
  stunted: the proportion of children under 5 years of age who are stunted (low height for 
  stunting (low height for age), reflecting chronic undernutrition
    > INFANT MORTALITY: the mortality rate of children under 5 years of age. 
  under 5 years old
  The sources for these data are the Food and Agriculture Organization of the United Nations 
  Food and Agriculture Organization (FAO), World Health Organization (WHO), UNICEF, World Bank, Demographic and Health Surveys (DHS) 
  Demographic and Health Surveys (DHS), and the United Nations Interagency Group on Child Mortality Estimation (UN IGME). 
  (UN IGME). The 2019 GHI is calculated for 117 countries with available data 
  are available and reflects data collected between 2014 and 2018.
  GHI countries are ranked on a scale from 0 to 100 
  points, with 0 being the best score (no hunger) and 100 being the worst, although 
  neither of these two extremes actually holds true. Scores 
  below 10.0 reflect a low level of hunger, scores from 10.0 to 19.9 a 
  19.9 indicate moderate hunger, scores from 20.0 to 34.9 indicate severe hunger 
  scores from 35.0 to 49.9 indicate an alarming level, and scores above 50 indicate 
  scores above 50 an extremely alarming level.

     GHI<=9.9: low severity - 10<GHI<19.9: moderate - 20<GHI<34.9: serious - 35<GHI<49.9: alarming - GHI > 50: alarming

![image](https://user-images.githubusercontent.com/80876493/234910567-e6c83cd1-e779-445b-9e82-ffad11cce648.png)

DATASET :

- Prevalence of undernourishment (% of population)
    Data (worldbank.org) : https://data.worldbank.org/indicator/SN.ITK.DEFC.ZS?view=chart

- The Global Hunger Index (GHI) :
    https://www.globalhungerindex.org/download/all.html
    Kaggle dataset open source : https://www.kaggle.com/datasets/whenamancodes/the-global-hunger-index?select=share-of-children-underweight.csv
    Article%20indicateurs%20GHI.pdf
    
- Infant mortality rate - UNICEF Data Warehouse
    https://data.unicef.org/resources/data_explorer/unicef_f/?ag=UNICEF&df=GLOBAL_DATAFLOW&ver=1.0&dq=.CME_MRY0..&startPeriod=2011&endPeriod=2021

- Kaggle dataset open source - Food Bank of the World:
    https://www.kaggle.com/datasets/pranav941/-world-food-wealth-bank

- World Health Organization Data Platform - Nutritional Deficiencies
    https://platform.who.int/mortality/themes/theme-details/topics/topic-details/MDB/nutritional-deficiencies
    
- GDP, PPP(Current international $) from 2000 to 2021
    https://donnees.banquemondiale.org/indicator/NY.GDP.MKTP.PP.CD

- SDG Indicators Database (SDG for sustainable development goal)(ODD2)

    API : https://unstats.un.org/sdgs/UNSDGAPIV5/swagger/index.html

    (https://www.agenda-2030.fr/17-objectifs-de-developpement-durable/article/odd2-eliminer-la-faim-assurer-la-securite-alimentaire-ameliorer-la-nutrition-et#:~:text=ODD2%20-%20%C3%89liminer%20la%20faim%2C%20assurer%20la%20s%C3%A9curit%C3%A9,une%20alimentation%20s%C3%BBre%2C%20nutritive%20et%20suffisante%20pour%20tous.)

    https://view.officeapps.live.com/op/view.aspx?  src=https%3A%2F%2Funstats.un.org%2Fsdgs%2Findicators%2FGlobal%2520Indicator%2520Framework%2520after%25202023%2520refinement.French.xlsx&wdOrigin=BROWSELINK

****************************************************************************************************************************************

3-DIMENSIONAL ANALYSIS  :

    I/ INTRODUCTION BY VISUALISATION : Tableau / Python / Matplotlib/ Seaborn

      Which countries and category of population are the most affected by Nutritional deficiencies ? By Food insecurity ? And By hunger ?

    II/ CORRELATION VS CAUSALITY : Python/SQL

      1/ Wealth/hungry : "Are there correlations between the GDP and GHI(global hunger index) indicators ? Is there a correlation between country GDP and high       prevalence of undernourishment?"

        2/ self-sufficiency in food : "are we producing enough?"

        3/ External impacts (COVID19, Severe natural damage, wars, ...)
            What are the aggravating factors?
            
    III/ Is SDG2 on the right track to eradicate hunger in the world by 2030? : API/ Python / Flask / Scipy / Web Scraping : requests, BeautifulSoup
          

*********************************************************************************
