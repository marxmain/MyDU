# TerritoriesConfig:
```yaml
TerritoriesConfig:
  parent: FeaturesConfig
  territoryUnitDeployDuration: 60
  territoryUnitRetrieveCooldown: 604800
  orgFirstTerritoryFee: 50000
  orgTerritoryFeeFactor: 50000
  orgTerritoryFeeExponant: 0
  playerFirstTerritoryFee: 0
  playerTerritoryFeeFactor: 50000
  playerTerritoryFeeExponant: 0
  initialExpirationDelayDays: 3
  maxBalanceInFeeDays: 90
  requisitionDelayDays: 14
  upkeepIntervalDays: 30
  upkeepFee: 10000
```
# IndustryConfig:
```yaml
IndustryConfig:
  parent: FeaturesConfig
  minRecipeTime: 1 # 30
```
# ReconnectRewardConfig:
```yaml
ReconnectionRewardConfig:
  parent: FeaturesConfig
  reconnectionRewardInterval: 82800
  reconnectionRewardMoney: 200000
```
# FetchConstructConfig:
```yaml
FetchConstructConfig:
  parent: FeaturesConfig
  hasTimeLimit: false # true
  fromPlanetSurface: true
  delay: 30 # 86400
  maxDistance: 10000 # 4000
```
# ConstructCompactionConfig:
```yaml
ConstructCompactionConfig:
  parent: FeaturesConfig
  autoCompactRadius: 0
  autoCompactionMinIdleTime: 10800
  compactionMaxMass: 100000 # 20000
```
