from cybernews.cybernews import CyberNews
import cybernews 
import fontstyle

# -----------------------------------------------------------
# this gives out list it seems ~TypeError: list indices must be integers or slices, not str
def _select_category(category):
    """Creates a Instance of the CyberNews and SELECTS the mentioned category and Returns it"""
    news = CyberNews()
    _categoryContent = news.get_news(category)
    return _categoryContent
# -----------------------------------------------------------
# -----------------------------------------------------------
# -----------------------------------------------------------
# -----------------------------------------------------------
# list of possible news categories
'''
| 1 | General News | news.get_news("general") |
| 2 | Data Breach News | news.get_news("dataBreach") |
| 3 | Cyber Attack News | news.get_news("cyberAttack") |
| 4 | Vulnerability News | news.get_news("vulenrability")|
| 5 | Malware News | news.get_news("malware") |
| 6 | Security News | news.get_news("security") |
| 7 | Cloud News | news.get_news("cloud") |
| 8 | Tech News | news.get_news("tech") |
| 9 | IOT News | news.get_news("iot") |
| 10 | Big Data News | news.get_news("bigData") |
| 11 | Business News | news.get_news("business") |
| 12 | Mobility News | news.get_news("mobility") |
| 13 | Research News | news.get_news("research") |
| 14 | Corporate News | news.get_news("corporate") |
| 15 | Social Media News | news.get_news("socialMedia") |
'''
# =================================================================================
# all from perticular categories
# def print_all_contents_of(this,fromThis,withColor="blue"):
#     """Interface for the content Printing.!!   from a categoryContent. """
#     _newsContent = _select_category(fromThis)
#     print(f"""News From: \"{fromThis}\"""")
#     for news in _newsContent:
#         print(fontstyle.apply(f"{news.get(this)}",f'bold/{withColor}' ))
# =================================================================================


# =================================================================================
# enumerate does the traversing and counting along with it.
def print_all_contents_of(this,fromThis,withColor="blue"):
    """Interface for the content Printing.!!   from a categoryContent. """
    _newsContent = _select_category(fromThis)
    print(f"""News From: \"{fromThis}\"""")
    for serial,news in enumerate(_newsContent):
        print(fontstyle.apply(f"{serial + 1} {news.get(this)}",f'bold/{withColor}' ))
# =================================================================================

# =================================================================================
# this based on the category prints either latest or Top Five News.
def print_news_from(category,latest=True):
    """Prints news from the given category based on weather latest or not
        if latest just prints LATEST i.e top 2 news
        if not latest prints TOPNEWS i.e top 5 news """
    _TOPNEWS = 5
    _LATEST = 2 
    """Improvement would be, to fetch the news based on TIME i.e to compare the dates 
    and decide for accurate latest news"""


    _newsContent = _select_category(category)
    if not latest:
        print(f"""
    
    Here are TOP FIVE News on \"{category}\"""")
        for _serial, news in enumerate(_newsContent):
            if _serial == _TOPNEWS:
                break
            print(f"""
                    ------------------------------------------------------------------
                    {fontstyle.apply(f"{news.get('headlines')}",'bold/Italic/blue')}
                    {fontstyle.apply(f"date: {news.get('newsDate')}",'faint/Italic')}
                    {fontstyle.apply(f"{news.get('newsURL')}",'white/blue_bg/Italic')}

                    {fontstyle.apply(f"{news.get('fullNews')}",'black/white_bg')}
                    """)
    else:
        print(f"""
    
    Here are LATEST News on \"{category}\"""")
        for _serial, news in enumerate(_newsContent):
            if _serial == _LATEST:
                break
            print(f"""
                    ------------------------------------------------------------------
                    {fontstyle.apply(f"{news.get('headlines')}",'bold/Italic/blue')}
                    {fontstyle.apply(f"date: {news.get('newsDate')}",'faint/Italic')}
                    {fontstyle.apply(f"{news.get('newsURL')}",'white/blue_bg/Italic')}

                    {fontstyle.apply(f"{news.get('fullNews')}",'black/white_bg')}
                    """)
# =================================================================================

# =================================================================================
def menu():
    print(f"""
    CYBERNEWS~ 
           select category:
    1. cyberAttack      5. security
    2. vulenrability    6. general
    3. tech             7. business
    4. malware          8. research
    {fontstyle.apply('note: by default latest news will be displayed.','FAINT/ITALIC')}
        """)
def switcher(option):
    cat = {
        1 : 'cyberAttack',
        2 : 'vulnerability',
        3 : 'tech',
        4 : 'malware',
        5 : 'security',
        6 : 'general',
        7 : 'business',
        8 : 'research'
    }
    return cat.get(option)
#============================================================================
# program starts here..
"""
FUTURE SCOPE:
One Major improvement can be, not to ask any category and all, 
giving THE LATEST news automatically searching from across various domains

for instance:  __interface would be like__

THE LATEST cybernews, from ANY CATEGORY !! (__Automatically, Not even have to Enter anything__)
(when i say latest, its based on relative TIME, more recent the INCIDENT more LATEST it is)
"""
if __name__ == "__main__":
    # print_all_contents_of("headlines",fromThis="security",withColor="red")
    ERR = 'RED/ITALIC'
    PRM = 'BLACK/GRAY_BG'
    menu()
#============================================================================
    while True:
        try:
            inQ = 'Category >>'
            option = int(input(fontstyle.apply(inQ,PRM)))
            break
        except ValueError:
            mes = 'NOT VALID!! Enter category number !! (example: 1)'
            print(fontstyle.apply(mes,ERR))
        except KeyboardInterrupt:
            mes = '\n ..exited'
            print(fontstyle.apply(mes,ERR))
            exit(1)
#============================================================================
    try:
        category = switcher(option)
    except NameError:
        mes = 'to use type >> python get_cybernews.py\n'
        print(fontstyle.apply(mes,ERR))
#============================================================================
    inQ = f'Do You want TOP 5 news under \"{category}\" (yes or no) NCS >>'
    srno = input(fontstyle.apply(inQ,PRM))
    srno = srno.lower()
    if srno == 'no' or srno == 'n':
        flag = True # meaning Latest NEWS 
    elif srno == 'yes' or srno == 'y':
        flag = False # meaning TOP 5 NEWS
    else:
        mes = 'That was yes or no Question !!'
        print(fontstyle.apply(mes,ERR))
#============================================================================
    try:
        print_news_from(category,flag)
    except:
        mes = 'only put category/Option that was Mentioned, dont assume your own.'
        print(fontstyle.apply(mes,ERR))
#============================================================================
