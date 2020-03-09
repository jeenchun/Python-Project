# Corona-Price-Tracker

This is our branch for the development of our Project Proposal and Outline for the Corona-Price-Tracker.
Team: E, J, I, T

Hi All,

Welcome to the Corona-Price-Tracker. Here we present our Python project for the HSOG Intro to Python Class. It splits into three parts: I. Project Description, II. Project Realisation, III. Milestones.

## I. Project Description

# I. Project Proposal

End of last year (2019), a novel coronavirus - the so-called COVID-19 - broke out in Wuhan, China. Since then, the virus has been constantly spreading and cases have been confirmed in over 90 countries to date (updated 3/10/2020[1]). This partially resulted in panic buying and regional shortages of hygiene and durable products. Given its unexpected emergence and rapid expansion, media outlets, health organizations as well as government authorities are providing nearly real-time information online to keep the global public informed. Due to local product shortages, consumption patterns (e.g. of masks, disinfectant, toilet paper etc.) have largely shifted to online shops, which makes a close analysis possible.
In Germany several public and private institutions are collecting, preparing and digitally publishing information on different aspects of the Coronavirus for the population. In particular, the Robert Koch Institut, the government’s central scientific institution in the field of public health, is keeping track of confirmed cases within Germany [2]; the Federal Centre for Health Education is providing answers to frequently asked questions with respect to COVID-19 [3]; the Federal Ministry of Foreign Affairs compiles information for travellers[4]; and the media outlet Handelsblatt gives a regular update on the economic impact of the coronavirus – they even created a specific newsletter for this.
However, while some websites (e.g. of the Federal Ministry of Health [5]) do refer to the different sources at hand (including the above mentioned), there is no platform yet that bundles the different kinds of public health, economic and individual information in one platform. The aim of our project is to fill this gap. In a nutshell, we plan to create a platform that provides three services:
First, it will display constantly-updated, general information about coronavirus-related developments in Germany. This may include i) confirmed coronavirus cases across German Federal States, with RKI data ii) national infections and recoveries from other sources such as JHU iii) the effects of the coronavirus on the German financial market, as well as iv) supermarket product price fluctuations and availability of durable goods (tracking & visualization of panic buying).
Second, the platform will be able to generate on-request, personalized information. Based on a user’s input, he or she may receive information, among others, on most recent official behaviour protocols, official health authority contacts and/or risk levels for the area of residence or interest.
Third, the platform may integrate an alert function for a realistic risk analysis when it comes to attendance  of big events (conferences, football matches) and public institutions (schools, universities). Users may be able to select certain parameters and in case these exceed predetermined limits, he or she is informed about the risk to go there.

# II. Realisation

The realisation of this project splits into three parts: data selection, data collection and data processing.
Data Selection – The first step toward our information platform is to define credible sources of information and to select their key data such as on the ‘number of confirmed cases’ and ‘price fluctuations’ in Germany. The selection of these focal points is ongoing and further depends on data access and availability, and is guided by moral and societal principles. So far, we closely monitor contributions from the Robert Koch Institute [2] , the World Health Organization [7] and Johns Hopkins University [1]. When it comes to make use of the latter, we have already identified the corresponding GitHub repository [8]. In addition, we will monitor media services such as newsletters and interactive maps provided by Tagesschau [9], Die ZEIT [10] and Handelsblatt [11]. The second step of our project is to track the development of good prices such as hygiene articles and durable goods. Since many german supermarkets are sold out, this consumer behavior has shifted to internet purchases. This allows us to track the consumer pattern of these products for example, at Amazon. Above all, our project shall contribute positively to society, for example by simplifying access to and processing of credible sources of information.
 Data collection – Secondly, we intend to collect the data by using web scraping with the Python Reddit API Wrapper (PRAW). This python package that allows us to access the reddit’s API. For example, we intend to scrape data from the RKI webpage using PRAW, to plot the development of different data points from German Federal States over time. 
For the public health data we strive to use the relevant information from the RKI and JHU [1&2]. For the development of selected good prices we intend to scrape data from the python-amazon-simple-product-api 2.2.11 [12]. Lastly we plan to include some basic user Input such as name, postcode, gender and age to generate a more individualized profile. 
Data processing – Thirdly, we plan to visualize the relevant information in one single platform. The output could potentially look like different graphs, maps and curves in one interface. The added value of our interface comes from processing multiple developments in one simple interface according to the user need without requiring research and consultation of each website individually. For example, we aim that a user from Berlin sees the following information in one interface: number of current corona cases in Berlin but also the development over time, the official protocol and phone number of Berlin health authorities, the availability and price for hygiene/ durable products online and the risk to get infected by attending the next football match of Union Berlin or Hertha BSC. However, this is work in progress and depends on the availability of the data we get from the APIs and how we decide to process them.

# III. Next steps / Milestones

- Product definition: information platform, define relevant project components
- Division of tasks and roles in the group, ensure contribution and management of GitHub repository
- Obtain relevant Python and Reddit Knowledge, Create Reddit Account to use PRAW [6] for data collection and processing
- Implement data collection with PRAW, monitor and evaluate data access and quality
- Write Pseudocode for data processing
- Coding for data processing: From API into platform
- Monitor feasibility, access to and use of relevant online API
- Develop final output, visualization of different components 
- Testing demo
 
 

[1] Cf. Coronavirus COVID-19 Global Cases by John Hopkins CSSE, accessible from: https://www.arcgis.com/apps/opsdashboard/index.html#/bda7594740fd40299423467b48e9ecf6 
[2] https://www.rki.de/DE/Content/InfAZ/N/Neuartiges_Coronavirus/Fallzahlen.html 
[3] https://www.infektionsschutz.de/coronavirus-sars-cov-2.html 
[4] https://www.auswaertiges-amt.de/de/ReiseUndSicherheit/covid-19/2296762 
[5] https://www.bundesgesundheitsministerium.de/coronavirus.html
[6] https://praw.readthedocs.io/en/latest/index.html 
[7] https://www.who.int/westernpacific/emergencies/covid-19 
[8] https://github.com/CSSEGISandData/COVID-19 
[9] https://www.tagesschau.de/inland/coronavirus-karte-deutschland-101.html 
[10] https://www.zeit.de/wissen/gesundheit/2020-03/coronavirus-deutschland-infektionen-faelle-verbreitung-epidemie-karte 
[11] https://www.handelsblatt.com/politik/international/coronavirus-die-aktuelle-lage-939-corona-faelle-in-deutschland-spahn-empfiehlt-absage-von-grossveranstaltungen/25483702.html 
[12] https://pypi.org/project/python-amazon-simple-product-api/ & https://github.com/yoavaviram/python-amazon-simple-product-api 



Cheers
E, I, J, T
