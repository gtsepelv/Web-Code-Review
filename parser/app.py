from flask import Flask, render_template
import requests
from pymongo import MongoClient

client = MongoClient("mongodb", 27017)
db = client.citilink
collection = db.products

app = Flask(__name__)


@app.route("/")
def index():
    data = collection.find()
    return render_template("index.html", data=data)


cookies = {
    "_tuid": "d1e98feaf9dc5b0b09d5ccef2a545cb32ac6ed9c",
    "_space": "yos_cl",
    "_city_guessed": "1",
    "_slid": "64176e8803f36936c3083ddd",
    "tmr_lvid": "3a8b6ccd07e01db3f417f2318b1a617c",
    "tmr_lvidTS": "1679257224937",
    "_userGUID": "0:lffue7fy:dlw3N2yqVC1o_1_OwBChRd9ovhD2ekYB",
    "_ym_uid": "1679257225874359342",
    "__exponea_etc__": "e3584ec4-09de-4159-aa3d-8a87f0b0faf4",
    "old_design": "0",
    "_slid_server": "64176e8803f36936c3083ddd",
    "digi_uc": "W1sidiIsIjE4OTE3MDkiLDE2NzkyNTcyNjQ1MjldLFsidiIsIjE4OTE3MDgiLDE2NzkyNTcyNTM4NDVdLFsidiIsIjE4OTAyMzUiLDE2NzkyNTczNTI5MDddXQ==",
    "rr_rcs": "v%3A%3A1679257264640%3Bv%3A1890235%3A1679257353172",
    "_slfreq": "6347f312d9062ed0380b52dc%3A6347f38c9a3f3b9e90027775%3A1680591229",
    "mindboxDeviceUUID": "942ded33-54a2-4e20-84ca-8ee9d388b9b7",
    "directCrm-session": "%7B%22deviceGuid%22%3A%22942ded33-54a2-4e20-84ca-8ee9d388b9b7%22%7D",
    "flocktory-uuid": "ddeb40ee-865c-4414-8a84-327dbe884dbe-5",
    "_ym_d": "1696857038",
    "_gpVisits": '{"isFirstVisitDomain":true,"todayD":"Sun%20Mar%2019%202023","idContainer":"100025C7"}',
    "advcake_track_id": "1e309448-4068-0995-29f9-2602a30dd373",
    "advcake_session_id": "a386c58a-fdc2-7358-d8f2-373d5c98625f",
    "advcake_track_url": "https%3A%2F%2Fwww.citilink.ru%2F",
    "advcake_utm_partner": "",
    "advcake_utm_webmaster": "",
    "advcake_click_id": "",
    "_gid": "GA1.2.1282359590.1707829705",
    "ab_test": "90x10v4%3A1%7Creindexer%3A1%7Cdynamic_yield%3A1%7Cwelcome_mechanics%3A4%7Cdummy%3A10",
    "ab_test_analytics": "90x10v4%3A1%7Creindexer%3A1%7Cdynamic_yield%3A1%7Cwelcome_mechanics%3A4%7Cdummy%3A10",
    "ab_test_segment": "72",
    "_sp_ses.faaa": "*",
    "_ym_isad": "1",
    "__exponea_time2__": "0.28730034828186035",
    "tmr_detect": "1%7C1707920950948",
    "_ga": "GA1.2.297471817.1679257225",
    "_sp_id.faaa": "2c892785-b0b6-4678-8842-a519112bec85.1679257225.8.1707922591.1707852154.35358730-2e79-4501-8b83-845f97fc43af.f12bd56c-8d1b-4632-99a2-c74123cb4137.e9e9b9ba-0fd0-4624-a0f1-12cae6de479a.1707918700205.55",
    "_ga_DDRSRL2E1B": "GS1.1.1707918700.8.1.1707922798.60.0.0",
    "_ga_DDRSRL2E1B-DG": "GS1.1.1707918700.4.1.1707922798.0.0.0",
}

headers = {
    "authority": "www.citilink.ru",
    "accept": "*/*",
    "accept-language": "ru,en;q=0.9",
    "cache-control": "no-cache",
    "content-type": "application/json",
    # 'cookie': '_tuid=d1e98feaf9dc5b0b09d5ccef2a545cb32ac6ed9c; _space=yos_cl; _city_guessed=1; _slid=64176e8803f36936c3083ddd; tmr_lvid=3a8b6ccd07e01db3f417f2318b1a617c; tmr_lvidTS=1679257224937; _userGUID=0:lffue7fy:dlw3N2yqVC1o_1_OwBChRd9ovhD2ekYB; _ym_uid=1679257225874359342; __exponea_etc__=e3584ec4-09de-4159-aa3d-8a87f0b0faf4; old_design=0; _slid_server=64176e8803f36936c3083ddd; digi_uc=W1sidiIsIjE4OTE3MDkiLDE2NzkyNTcyNjQ1MjldLFsidiIsIjE4OTE3MDgiLDE2NzkyNTcyNTM4NDVdLFsidiIsIjE4OTAyMzUiLDE2NzkyNTczNTI5MDddXQ==; rr_rcs=v%3A%3A1679257264640%3Bv%3A1890235%3A1679257353172; _slfreq=6347f312d9062ed0380b52dc%3A6347f38c9a3f3b9e90027775%3A1680591229; mindboxDeviceUUID=942ded33-54a2-4e20-84ca-8ee9d388b9b7; directCrm-session=%7B%22deviceGuid%22%3A%22942ded33-54a2-4e20-84ca-8ee9d388b9b7%22%7D; flocktory-uuid=ddeb40ee-865c-4414-8a84-327dbe884dbe-5; _ym_d=1696857038; _gpVisits={"isFirstVisitDomain":true,"todayD":"Sun%20Mar%2019%202023","idContainer":"100025C7"}; advcake_track_id=1e309448-4068-0995-29f9-2602a30dd373; advcake_session_id=a386c58a-fdc2-7358-d8f2-373d5c98625f; advcake_track_url=https%3A%2F%2Fwww.citilink.ru%2F; advcake_utm_partner=; advcake_utm_webmaster=; advcake_click_id=; _gid=GA1.2.1282359590.1707829705; ab_test=90x10v4%3A1%7Creindexer%3A1%7Cdynamic_yield%3A1%7Cwelcome_mechanics%3A4%7Cdummy%3A10; ab_test_analytics=90x10v4%3A1%7Creindexer%3A1%7Cdynamic_yield%3A1%7Cwelcome_mechanics%3A4%7Cdummy%3A10; ab_test_segment=72; _sp_ses.faaa=*; _ym_isad=1; __exponea_time2__=0.28730034828186035; tmr_detect=1%7C1707920950948; _ga=GA1.2.297471817.1679257225; _sp_id.faaa=2c892785-b0b6-4678-8842-a519112bec85.1679257225.8.1707922591.1707852154.35358730-2e79-4501-8b83-845f97fc43af.f12bd56c-8d1b-4632-99a2-c74123cb4137.e9e9b9ba-0fd0-4624-a0f1-12cae6de479a.1707918700205.55; _ga_DDRSRL2E1B=GS1.1.1707918700.8.1.1707922798.60.0.0; _ga_DDRSRL2E1B-DG=GS1.1.1707918700.4.1.1707922798.0.0.0',
    "origin": "https://www.citilink.ru",
    "pragma": "no-cache",
    "referer": "https://www.citilink.ru/catalog/smartfony/?sorting=price_asc&pf=ms_action%2Cdiscount.any%2Crating.any&f=ms_action%2Cdiscount.any%2Crating.any%2Capple",
    "sec-ch-ua": '"Not_A Brand";v="8", "Chromium";v="120", "YaBrowser";v="24.1", "Yowser";v="2.5"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": '"Windows"',
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 YaBrowser/24.1.0.0 Safari/537.36",
}

json_data = {
    "query": "query GetSubcategoryProductsFilter($subcategoryProductsFilterInput:CatalogFilter_ProductsFilterInput!,$categoryFilterInput:Catalog_CategoryFilterInput!,$categoryCompilationFilterInput:Catalog_CategoryCompilationFilterInput!){productsFilter(filter:$subcategoryProductsFilterInput){record{...SubcategoryProductsFilter},error{... on CatalogFilter_ProductsFilterInternalError{__typename,message},... on CatalogFilter_ProductsFilterIncorrectArgumentsError{__typename,message}}},category(filter:$categoryFilterInput){...SubcategoryCategoryInfo}}fragment SubcategoryProductsFilter on CatalogFilter_ProductsFilter{__typename,products{...ProductSnippetFull},sortings{id,name,slug,directions{id,isSelected,name,slug,isDefault}},groups{...SubcategoryProductsFilterGroup},compilations{popular{...SubcategoryProductCompilationInfo},brands{...SubcategoryProductCompilationInfo},carousel{...SubcategoryProductCompilationInfo}},pageInfo{...Pagination},searchStrategy}fragment ProductSnippetFull on Catalog_Product{...ProductSnippetShort,propertiesShort{...ProductProperty},rating,counters{opinions,reviews}}fragment ProductSnippetShort on Catalog_Product{...ProductSnippetBase,labels{...ProductLabel},delivery{__typename,self{__typename,availabilityByDays{__typename,deliveryTime,storeCount}}},stock{stores{__typename,list{store{id,shortName2,isFavorite},count},count},countInStores,maxCountInStock}}fragment ProductSnippetBase on Catalog_Product{id,name,shortName,slug,isAvailable,images{citilink{...Image}},price{...ProductPrice},category{id,name},brand{name},multiplicity,quantityInPackageFromSupplier}fragment Image on Image{sources{url,size}}fragment ProductPrice on Catalog_ProductPrice{current,old,club,clubPriceViewType}fragment ProductLabel on Catalog_Label{id,type,title,description,target{...Target},textColor,backgroundColor,expirationTime}fragment Target on Catalog_Target{action{...TargetAction},url,inNewWindow}fragment TargetAction on Catalog_TargetAction{id}fragment ProductProperty on Catalog_Property{name,value}fragment SubcategoryProductsFilterGroup on CatalogFilter_FilterGroup{id,isCollapsed,isDisabled,name,filter{... on CatalogFilter_ListFilter{__typename,isSearchable,logic,filters{id,isDisabled,isInShortList,isInTagList,isSelected,name,total,childGroups{id,isCollapsed,isDisabled,name,filter{... on CatalogFilter_ListFilter{__typename,isSearchable,logic,filters{id,isDisabled,isInShortList,isInTagList,name,isSelected,total}},... on CatalogFilter_RangeFilter{__typename,fromValue,isInTagList,maxValue,minValue,serifValues,toValue,unit}}}}},... on CatalogFilter_RangeFilter{__typename,fromValue,isInTagList,maxValue,minValue,serifValues,toValue,unit}}}fragment SubcategoryProductCompilationInfo on CatalogFilter_CompilationInfo{__typename,compilation{...SubcategoryProductCompilation},isSelected}fragment SubcategoryProductCompilation on Catalog_ProductCompilation{__typename,id,type,name,slug,parentSlug,seo{h1,title,text,description}}fragment Pagination on PageInfo{hasNextPage,hasPreviousPage,perPage,page,totalItems,totalPages}fragment SubcategoryCategoryInfo on Catalog_CategoryResult{... on Catalog_Category{...Category,seo{h1,title,text,description},compilation(filter:$categoryCompilationFilterInput){... on Catalog_CategoryCompilation{__typename,id,name,seo{h1,title,description,text}},... on Catalog_CategoryCompilationIncorrectArgumentError{__typename,message},... on Catalog_CategoryCompilationNotFoundError{__typename,message}}},... on Catalog_CategoryIncorrectArgumentError{__typename,message},... on Catalog_CategoryNotFoundError{__typename,message}}fragment Category on Catalog_Category{__typename,id,name,slug}",
    "variables": {
        "subcategoryProductsFilterInput": {
            "categorySlug": "smartfony",
            "compilationPath": [],
            "pagination": {
                "page": 1,
                "perPage": 48,
            },
            "conditions": [
                {
                    "filterGroupId": "",
                    "filterIds": [
                        "ms_action",
                        "discount.any",
                        "rating.any",
                        "apple",
                    ],
                },
            ],
            "sorting": {
                "id": "price",
                "direction": "SORT_DIRECTION_ASC",
            },
            "popularitySegmentId": "THREE",
        },
        "categoryFilterInput": {
            "slug": "smartfony",
        },
        "categoryCompilationFilterInput": {
            "slug": "",
        },
    },
}

response = requests.post(
    "https://www.citilink.ru/graphql/", cookies=cookies, headers=headers, json=json_data
)


def get_data():
    products = {
        str(i["name"]): [i["price"]["current"]]
        for i in response.json()
        .get("data")
        .get("productsFilter")
        .get("record")
        .get("products")
    }

    # print(str(products).replace(", ", ",\n "))
    collection.delete_one(products)
    collection.insert_one(products)


get_data()


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
