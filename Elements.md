# Cores
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
  - name: ImprovedDynamicCoreUnitExpertise
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
  - name: ImprovedDynamicCoreUnitExpertise
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
  - name: ImprovedDynamicCoreUnitExpertise
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
  - name: ImprovedDynamicCoreUnitExpertise
    level: 4
  hitpoints: 21420
```
