from tabulate import tabulate

# 原始数据
data = {
    "GIT": {
        "Amazon-Engineering": 2186,
        "Meta-Engineering": 1023,
        "DataBricks-Engineering": 111,
        "Tiktok-US-Engineering": 97,
        "Snowflake-Engineering": 59,
        "Google-US-Engineering": 1547,
        "Bloomberg-US-Engineering&Information Technology": 186,
        "Microsoft-US-Engineering": 1412,
        "Uber-US-Engineering": 124,
        "Airbnb-Engineering": 56,
        "NVIDIA-Engineering": 366,
        "Oracle-Engineering": 238,
        "Salesforce-Engineering": 303
    },
    "UW": {
        "Amazon-Engineering": 2237,
        "Meta-Engineering": 786,
        "DataBricks-Engineering": 62,
        "Tiktok-US-Engineering": 79,
        "Snowflake-Engineering": 56,
        "Google-US-Engineering": 1035,
        "Bloomberg-US-Engineering&Information Technology": 49,
        "Microsoft-US-Engineering": 2386,
        "Uber-US-Engineering": 92,
        "Airbnb-Engineering": 59,
        "NVIDIA-Engineering": 139,
        "Oracle-Engineering": 241,
        "Salesforce-Engineering": 261
    },
    "UCLA": {
        "Amazon-Engineering": 998,
        "Meta-Engineering": 689,
        "DataBricks-Engineering": 63,
        "Tiktok-US-Engineering": 91,
        "Snowflake-Engineering": 19,
        "Google-US-Engineering": 1183,
        "Bloomberg-US-Engineering&Information Technology": 40,
        "Microsoft-US-Engineering": 396,
        "Uber-US-Engineering": 87,
        "Airbnb-Engineering": 60,
        "NVIDIA-Engineering": 168,
        "Oracle-Engineering": 174,
        "Salesforce-Engineering": 130
    },
    "UIUC": {
        "Amazon-Engineering": 1350,
        "Meta-Engineering": 750,
        "DataBricks-Engineering": 96,
        "Tiktok-US-Engineering": 96,
        "Snowflake-Engineering": 43,
        "Google-US-Engineering": 1275,
        "Bloomberg-US-Engineering&Information Technology": 122,
        "Microsoft-US-Engineering": 740,
        "Uber-US-Engineering": 105,
        "Airbnb-Engineering": 51,
        "NVIDIA-Engineering": 331,
        "Oracle-Engineering": 173,
        "Salesforce-Engineering": 183
    },
    "CMU": {
        "Amazon-Engineering": 1344,
        "Meta-Engineering": 1259,
        "DataBricks-Engineering": 148,
        "Tiktok-US-Engineering": 186,
        "Snowflake-Engineering": 59,
        "Google-US-Engineering": 2162,
        "Bloomberg-US-Engineering&Information Technology": 160,
        "Microsoft-US-Engineering": 653,
        "Uber-US-Engineering": 127,
        "Airbnb-Engineering": 105,
        "NVIDIA-Engineering": 370,
        "Oracle-Engineering": 274,
        "Salesforce-Engineering": 210
    }
}

# 提取学校和公司名称
schools = list(data.keys())
companies = list(data[schools[0]].keys())

# 准备表格数据，添加总数列
table_data = []
for school in schools:
    row = [school]
    total = 0
    for company in companies:
        value = data[school][company]
        row.append(value)
        total += value
    row.append(total)
    table_data.append(row)

# 设置表头，添加总数列标题
headers = ["学校"] + companies + ["总数"]

# 使用tabulate库打印表格
print(tabulate(table_data, headers=headers, tablefmt="grid"))