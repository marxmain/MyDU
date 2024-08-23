# Cores
Larger Cores are unlocked via the Improved Core Unit Expertise talent. If you don't want that, then just delete required Talents.
## Static Cores
### CoreUnitStatic512:
```yaml
CoreUnitStatic512:
  parent: CoreUnitStatic
  constructSize: 512
  displayName: Static Core Unit
  cellSize: 0.5
  scale: xl # marxman: added: same size like L core
  level: 2 # marxman: changed from 1:
  unitVolume: 20008.00 # marxman: added: 8*L core volume
  unitMass: 97131.76 # marxman: added: 8*L core mass
  hidden: false # marxman: changed from 2:
  requiredTalents: # marxman: added:
  - name: StaticCoreUnitExpertise
    level: 5
  hitpoints: 21420 # marxman: changed from 50: 2*L core hitpoints
```
### CoreUnitStatic1024:
```yaml
CoreUnitStatic1024:
  parent: CoreUnitStatic
  constructSize: 1024
  displayName: Static Core Unit 512m
  cellSize: 1.0
  scale: xxl # marxman: added: same size like L core
  level: 4 # marxman: changed from 1:
  unitVolume: 20008.00 # marxman: added: 8*L core volume
  unitMass: 97131.76 # marxman: added: 8*L core mass
  hidden: false # marxman: changed from 2:
  requiredTalents: # marxman: added:
  - name: ImprovedCoreUnitExpertise
    level: 1
  hitpoints: 21420 # marxman: changed from 50: 2*L core hitpoints
```
### CoreUnitStatic2048:
```yaml
CoreUnitStatic2048:
  parent: CoreUnitStatic
  constructSize: 2048
  displayName: Static Core Unit 1024m
  cellSize: 2.0
  scale: xxxl # marxman: added: same size like L core
  level: 4 # marxman: changed from 1:
  unitVolume: 20008.00 # marxman: added: 8*L core volume
  unitMass: 97131.76 # marxman: added: 8*L core mass
  hidden: false # marxman: changed from 2:
  requiredTalents: # marxman: added:
  - name: ImprovedCoreUnitExpertise
    level: 2
  hitpoints: 21420 # marxman: changed from 50: 2*L core hitpoints
```
### CoreUnitStatic4096:
```yaml
CoreUnitStatic4096:
  parent: CoreUnitStatic
  constructSize: 4096
  displayName: Static Core Unit 2048m
  cellSize: 4.0
  scale: xxxxl # marxman: added: same size like L core
  level: 4 # marxman: changed from 1:
  unitVolume: 20008.00 # marxman: added: 8*L core volume
  unitMass: 97131.76 # marxman: added: 8*L core mass
  hidden: false # marxman: changed from 2:
  requiredTalents: # marxman: added:
  - name: ImprovedCoreUnitExpertise
    level: 3
  hitpoints: 21420 # marxman: changed from 50: 2*L core hitpoints
```
### CoreUnitStatic8192:
```yaml
CoreUnitStatic8192:
  parent: CoreUnitStatic
  constructSize: 8192
  displayName: Static Core Unit 4096m
  cellSize: 8.0
  scale: xxxxxl
  level: 4
  unitVolume: 20008.00
  unitMass: 97131.76
  hidden: false
  requiredTalents:
  - name: ImprovedCoreUnitExpertise
    level: 4
  hitpoints: 21420
```
## Dynamic Cores
### CoreUnitDynamic512:
```yaml
CoreUnitDynamic512:
  parent: CoreUnitDynamic
  constructSize: 512
  displayName: Dynamic Core Unit
  cellSize: 0.5
  scale: xl # marxman: added: same size like L core
  level: 4 # marxman: changed from 1:
  unitVolume: 20008.00 # marxman: added: 8*L core volume
  unitMass: 97131.76 # marxman: added: 8*L core mass
  hidden: false # marxman: changed from 2:
  requiredTalents: # marxman: added:
  - name: DynamicCoreUnitExpertise
    level: 5
  hitpoints: 21420 # marxman: changed from 50: 2*L core hitpoints
```
### CoreUnitDynamic1024:
```yaml
CoreUnitDynamic1024:
  parent: CoreUnitDynamic
  constructSize: 512
  displayName: Dynamic Core Unit
  cellSize: 1.0
  scale: xxl # marxman: added: same size like L core
  level: 4 # marxman: changed from 1:
  unitVolume: 20008.00 # marxman: added: 8*L core volume
  unitMass: 97131.76 # marxman: added: 8*L core mass
  hidden: false # marxman: changed from 2:
  requiredTalents: # marxman: added:
  - name: ImprovedCoreUnitExpertise
    level: 1
  hitpoints: 21420 # marxman: changed from 50: 2*L core hitpoints
```
### CoreUnitDynamic2048
```yaml
CoreUnitDynamic2048:
  parent: CoreUnitDynamic
  constructSize: 2048
  displayName: Dynamic Core Unit 1024m
  cellSize: 2.0
  scale: xxxl # marxman: added: same size like L core
  level: 4 # marxman: changed from 1:
  unitVolume: 20008.00 # marxman: added: 8*L core volume
  unitMass: 97131.76 # marxman: added: 8*L core mass
  hidden: false # marxman: changed from 2:
  requiredTalents: # marxman: added:
  - name: ImprovedCoreUnitExpertise
    level: 2
  hitpoints: 21420 # marxman: changed from 50: 2*L core hitpoints
```
###  CoreUnitDynamic4096
```yaml
CoreUnitDynamic4096:
  parent: CoreUnitDynamic
  constructSize: 4096
  displayName: Dynamic Core Unit 2048m
  cellSize: 4.0
  scale: xxxxl # marxman: added: same size like L core
  level: 4 # marxman: changed from 1:
  unitVolume: 20008.00 # marxman: added: 8*L core volume
  unitMass: 97131.76 # marxman: added: 8*L core mass
  hidden: false # marxman: changed from 2:
  requiredTalents: # marxman: added:
  - name: ImprovedCoreUnitExpertise
    level: 3
  hitpoints: 21420 # marxman: changed from 50: 2*L core hitpoints
```
###  CoreUnitDynamic8192
```yaml
CoreUnitDynamic8192:
  parent: CoreUnitDynamic
  constructSize: 8192
  displayName: Dynamic Core Unit 4096m
  cellSize: 8.0
  scale: xxxxxl
  level: 4
  unitVolume: 20008.00
  unitMass: 97131.76
  hidden: false
  requiredTalents:
  - name: ImprovedCoreUnitExpertise
    level: 4
  hitpoints: 21420
```
# IndustryInfrastructure
## IndustryUnit
```yaml
IndustryUnit:
  parent: IndustryInfrastructure
  displayName: Industry
  isUseable: true
  productNameList: []
  description: Industry Units are used to craft advanced and powerful items. They can only be used on Static Constructs.
  visibilityLOD: 3
  resistances:
    antimatter: 0.0
    thermic: 0.0
    kinetic: 0.0
    electromagnetic: 0.0
  speedFactor: 0.1 # 1
  industryEfficiency: 0.1 # 1
```
## MiningUnit
```yaml
MiningUnit:
  parent: IndustryInfrastructure
  displayName: Mining units
  description: Mining Units can be deployed on constructs in appropriate territories in order to extract raw ore from territory tiles. Mining units will need to be regularly calibrated for optimal usage.
  visibilityLOD: 4
  calibrationGracePeriodHours: 72
  calibrationDecreaseRatePerHour: 0 # 0.00625
  isUseable: true
  miningEfficiency: 10.0 # 0.9
  adjacentTerritoryBonus: 0.25 # 0.1
  calibrationCooldownHour: 1 # 24
  pickupCooldownHour: 1 # 24
  stopCooldownHour: 1 # 24
```
### MiningUnitSmall
```yaml
MiningUnitSmall1:
  displayName: Basic Mining Unit
  scale: s
  level: 1
  parent: MiningUnit
  oreTier: 1
  miningEfficiency: 5.0
  unitMass: 180
  unitVolume: 70
  hitpoints: 2500
```

