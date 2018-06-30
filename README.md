# typo
### How it Works
A physical keyboard is simulated, with the qwerty layout<br>
Each key is represented by a 1x1 square in the following co-ordinate system:

| key | top-left corner coord |
|-----|-----------------------|
| q   | (0,0)                 |
| w   | (1,0)                 |
| e   | (2,0)                 |
| a   | (0,-1)                |
| s   | (1,-1)                |
| z   | (0,-2)                |
| ... | ...                   |

<small>I.e: 'q' is origin (0,0). Left = +x. Down = -y.</small><br>
NB: each row has an x offset of 0, 0.5, 1.5 respectively as well to simulate the positioning of the rows on physical keyboards.

For typo generation, a random vector is generated from (the centre of) a key, and which keys it 'intersects' and in which order is calculated.

### Usage
```python
print gen("the quick brown fox jumps over a lazy dog",n=2)
```
generates:
```
thbve quick brown fox jumps overfdr a lazy dog
```
| Arg  | Info                              |
|------|-----------------------------------|
| str  | string to be altered              |
| f1   | magnitude lower bound (def:0.5)   |
| f2   | magnitude upper bound (def:1.5)   |
| must | bool if typos must happen (def:1) |
| n    | number of typo iterations (def:1) |

NB: typos can only be performed on alphabetic characters. A string with no alphabetic characters will be returned unchanged.
NB: if must=0, typos actually are generated approx 68% of the time
