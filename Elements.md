# Cores
## Static Core
### CoreUnitDynamic512:
```yaml
CoreUnitStatic512:
  parent: CoreUnitStatic
  constructSize: 512
  displayName: Static Core Unit 256m
  cellSize: 0.5
  scale: 1 # marxman: added: same size like L core
  level: 2 # marxman: changed from 1:
  unitVolume: 20008.00 # marxman: added: 8*L core volume
  unitMass: 97131,76 # marxman: added: 8*L core mass
  hidden: false # marxman: changed from 2:
  requiredTalents: # marxman: added:
  - name: StaticCoreUnitExpertise
    level: 5
  hitpoints: 21420 # marxman: changed from 50: 2*L core hitpoints
```
