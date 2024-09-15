import json
import random

# Ore tiers and cluster settings
tier_1 = ["AluminiumOre", "CarbonOre", "IronOre", "SiliconOre"]
tier_2 = ["CalciumOre", "ChromiumOre", "CopperOre", "SodiumOre"]
tier_3 = ["LithiumOre", "NickelOre", "SilverOre", "SulfurOre"]
tier_4 = ["CobaltOre", "FlourineOre", "GoldOre", "ScandiumOre"]
tier_5 = ["ManganeseOre", "NiodiumOre", "TitaniumOre", "VanadiumOre", "ThoramineOre"]

# Cluster settings per ore tier
cluster_settings = {
    "tier_1": {"cluster_probability": 0.20, "decrease_probability": 0.05, "min_value": 200, "min_increase": 20, "max_increase": 40},
    "tier_2": {"cluster_probability": 0.15, "decrease_probability": 0.07, "min_value": 40, "min_increase": 15, "max_increase": 30},
    "tier_3": {"cluster_probability": 0.10, "decrease_probability": 0.10, "min_value": 8, "min_increase": 8, "max_increase": 16},
    "tier_4": {"cluster_probability": 0.10, "decrease_probability": 0.10, "min_value": 2, "min_increase": 4, "max_increase": 12},
    "tier_5": {"cluster_probability": 0.10, "decrease_probability": 0.10, "min_value": 1, "min_increase": 2, "max_increase": 10},
}

# Function to generate cluster values
def create_cluster_values(min_value, min_increase, max_increase, decrease_probability):
    values = []
    current_value = min_value
    increasing = True
    
    while True:
        if increasing:
            # Increase phase: randomly increase within the defined range
            increase = random.randint(min_increase, max_increase)
            current_value += increase
            values.append(current_value)

            # Ensure the value never drops to 0
            if current_value <= 0:
                current_value = min_value

            # Probability that the decrease phase starts
            if random.random() < decrease_probability:
                increasing = False
        else:
            # Decrease phase: randomly decrease, not below the minimum value
            decrease = random.randint(min_increase, max_increase)
            current_value = max(min_value, current_value - decrease)
            values.append(current_value)

            # Ensure the value never drops to 0
            if current_value <= 0:
                current_value = min_value

            # End the cluster if it reaches the minimum value
            if current_value == min_value:
                break

    return values

# Function to create the distribution across territories
def create_territory_distribution(territories, ore_presence):
    distribution = {}

    # Loop through all territories and assign values for each ore individually
    for i in range(territories):
        if str(i) not in distribution:
            distribution[str(i)] = {}

        # Loop through each tier and each ore separately
        for ore_list, settings_key in [(tier_1, "tier_1"), (tier_2, "tier_2"), (tier_3, "tier_3"), (tier_4, "tier_4"), (tier_5, "tier_5")]:
            settings = cluster_settings[settings_key]
            ore_list = [ore for ore in ore_list if ore_presence.get(ore, False)]

            for ore in ore_list:
                cluster_active = random.random() < settings["cluster_probability"]
                if cluster_active:
                    # Generate a new cluster for each ore independently
                    cluster_values = create_cluster_values(settings["min_value"], settings["min_increase"], settings["max_increase"], settings["decrease_probability"])

                    # Apply cluster values across territories
                    for j in range(len(cluster_values)):
                        if i + j < territories:
                            if str(i + j) not in distribution:
                                distribution[str(i + j)] = {}
                            distribution[str(i + j)][ore] = max(cluster_values[j], settings["min_value"])
                        else:
                            break
                else:
                    # Assign minimum values if no cluster is active
                    distribution[str(i)][ore] = settings["min_value"]

    return distribution

# Main function to get user input and generate the distribution
def main():
    # Ask for the file name
    file_name = input("Enter the file name to save the distribution (without extension): ") + ".json"
    
    # Ask for the number of territories
    territories = int(input("Enter the number of territories: "))
    
    # Ask for ore presence on the planet
    ore_presence = {}
    for ore_list, tier_name in zip([tier_1, tier_2, tier_3, tier_4, tier_5], ["Tier 1", "Tier 2", "Tier 3", "Tier 4", "Tier 5"]):
        for ore in ore_list:
            presence = input(f"Is {ore} (from {tier_name}) present on the planet? (y/n): ").strip().lower()
            ore_presence[ore] = presence == "y"
    
    # Generate the distribution based on the user input
    distribution = create_territory_distribution(territories, ore_presence)
    
    # Sorted distribution by ore types
    sorted_distribution = {}
    
    # List all ore tiers
    for ore_list, ore_settings in zip([tier_1, tier_2, tier_3, tier_4, tier_5], ["tier_1", "tier_2", "tier_3", "tier_4", "tier_5"]):
        for ore in ore_list:
            min_value = cluster_settings[ore_settings]["min_value"]
            if ore_presence.get(ore, False):
                sorted_distribution[ore] = {key: distribution.get(key, {}).get(ore, min_value) for key in distribution}
    
    # Save the results
    with open(file_name, 'w') as file:
        json.dump(sorted_distribution, file, indent=4)

    print(f"Ore distribution successfully created and saved as {file_name}.")

# Run the script
if __name__ == "__main__":
    main()
