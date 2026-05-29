def analyze_revenue(data: dict) -> str:
    """
    Analyze revenue performance
    """
    revenue = data.get("revenue", 0)
    previous = data.get("previous_revenue", 0)

    if previous == 0:
        return "No previous data to compare."

    growth = ((revenue - previous) / previous) * 100

    if growth > 0:
        return f"Revenue increased by {growth:.2f}%."
    elif growth < 0:
        return f"Revenue decreased by {abs(growth):.2f}%."
    else:
        return "Revenue is stable."


def customer_segmentation(customers: list) -> str:
    """
    Simple customer segmentation
    """
    high = [c for c in customers if c.get("spend", 0) > 1000]
    medium = [c for c in customers if 500 < c.get("spend", 0) <= 1000]
    low = [c for c in customers if c.get("spend", 0) <= 500]

    return (
        f"High-value customers: {len(high)}\n"
        f"Medium-value customers: {len(medium)}\n"
        f"Low-value customers: {len(low)}"
    )


def suggest_kpis(business_type: str) -> list:
    """
    Suggest KPIs based on business type
    """
    kpis = {
        "ecommerce": ["Conversion Rate", "Average Order Value", "Customer Lifetime Value"],
        "saas": ["MRR", "Churn Rate", "Customer Acquisition Cost"],
        "retail": ["Foot Traffic", "Sales per Square Foot", "Inventory Turnover"]
    }

    return kpis.get(business_type.lower(), ["Revenue Growth", "Customer Retention"])


# 🔥 TEST BLOCK
if __name__ == "__main__":
    print("Testing Business Tools...\n")

    # Revenue test
    print(analyze_revenue({
        "revenue": 12000,
        "previous_revenue": 10000
    }))

    print()

    # Customer segmentation test
    customers = [
        {"name": "A", "spend": 1200},
        {"name": "B", "spend": 700},
        {"name": "C", "spend": 300}
    ]

    print(customer_segmentation(customers))

    print()

    # KPI test
    print(suggest_kpis("ecommerce"))