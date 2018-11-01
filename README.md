# Circle Art

A tiny Python script to draw beautiful circles, with standard library `turtle`. [Demo here.](./demo.mp4)

### Usage

```
./cadraw.py [base radius] [circle list] [args...]
```

`base radius` is radius of base circle, which is the only full circle in the picture.

`circle list` is a list of triple tuples. For each tuple, the first element is either `'i'` or `'o'`. It indicates the circle is inside of base circle or outside of it. The second `n` and third `d` are two integers, which mean one component arc of current circle crosses `n/d` of perimeter of the circle it lives on.

Use `--preview` to draw circles super fastly, and use `--no-scale` to disable scaling action per circle.

----

Copyright &copy; 2018 Correctizer.
