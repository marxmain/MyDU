# Ore Pool Generator

This script generates a resource distribution (ore pool) for a planet with multiple territories, where the presence of ores and the number of territories are user-defined. The ore distribution is saved as a JSON file based on user input.

## Features
- The user defines the number of territories for the planet.
- The user specifies which ores are present on the planet.
- Ore distribution is determined using cluster-based probabilities for each ore tier.
- The final ore distribution is saved in a user-specified JSON file.

## Ore Tiers
The ores are grouped into five tiers, each with different probabilities for cluster formation and size.

- **Tier 1**: AluminiumOre, CarbonOre, IronOre, SiliconOre
- **Tier 2**: CalciumOre, ChromiumOre, CopperOre, SodiumOre
- **Tier 3**: LithiumOre, NickelOre, SilverOre, SulfurOre
- **Tier 4**: CobaltOre, FlourineOre, GoldOre, ScandiumOre
- **Tier 5**: ManganeseOre, NiodiumOre, TitaniumOre, VanadiumOre, ThoramineOre

## Usage

1. **Run the Script**: 
   ```bash
   python ore_pool_generator.py
   ```

2. **Enter Inputs**:
   - **File Name**: The script first asks for the name of the file where the generated ore distribution will be saved.
   - **Number of Territories**: Input the number of territories for the planet.
   - **Ore Presence**: For each ore, indicate whether it is present on the planet by typing `y` for yes or `n` for no.

3. **Output**: The script creates a JSON file with the ore distribution for each territory based on the user inputs. The file will be saved with the provided name.

## Example Interaction

```bash
Enter the file name to save the distribution (without extension): my_planet_resources
Enter the number of territories: 150
Is AluminiumOre (from Tier 1) present on the planet? (y/n): y
Is CarbonOre (from Tier 1) present on the planet? (y/n): n
Is IronOre (from Tier 1) present on the planet? (y/n): y
...
```

## Output

The output is a JSON file that contains the ore distribution for the specified number of territories. Each ore is assigned a resource value based on the probabilities and cluster logic.
