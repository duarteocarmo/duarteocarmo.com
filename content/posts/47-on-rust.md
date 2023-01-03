title: On Rust 
date: 2023-01-02
description: Thoughts on using Rust to solve AoC, from a Python programmer. 
status: published
slug: on-rust
thumbnail: images/47/rust_logo.png

It's that time of the year again. The family is getting together and celebrating. Grandma is cooking something amazing for dinner. I'm trying to solve [Advent of Code](https://adventofcode.com/) puzzles. This year, I decided to do something _different_. Instead of solving the puzzles in Python, I decided that I would try to solve them in [Rust](https://www.rust-lang.org/). Why?

Rust has been getting a lot of attention lately. The language is in its _7th_ year as the [most loved programming language](https://survey.stackoverflow.co/2022/#technology-most-loved-dreaded-and-wanted) according to the latest Stack Overflow developer survey. Why do people love it so much? So I decided to learn it. What better way to get frustrated during my Christmas break?

## Things I like

**Speed.** That's the first thing I noticed. I brute force _a lot_ of these AoC puzzles. Rust handled them without hiccups. It's a bit like the feeling of using Numpy if you're a Python dev. Having been one for some years, I never got much exposure to compiled languages like C++ or Java. I can't help but notice a pretty big difference in speed compared to Python or JavaScript.

**Effectiveness.** Most puzzles I solved were right on the first try. This is rarely the case with Python. Rather than using types as more of a _decorative/ergonomic_ feature like in Python, in Rust, these types are strictly enforced at compile time. This made me think twice about the code I wrote. But also lead to more correct code. [Rust-analyzer](https://rust-analyzer.github.io/), Rust's LSP, was also a great experience. Giving timely, useful, and clear messages about what was wrong. 

**Syntax.** The syntax is not that different from Python. For loops are easy and readable with the `for x in y` syntax, for example. [Closures](https://doc.rust-lang.org/beta/rust-by-example/fn/closures.html) remind me a lot of lambda functions in Python. I can also see why Python adopted the [match](https://doc.rust-lang.org/rust-by-example/flow_control/match.html) statement. In general, Rust was readable. Whenever code got complicated and repetitive, things like [macros](https://doc.rust-lang.org/rust-by-example/macros.html) came to the rescue. 

**Ecosystem.** Compared to Pip, [Cargo](https://doc.rust-lang.org/cargo/guide/index.html) is a breath of fresh air. Installing packages is as easy as copy-pasting into your `Cargo.toml` file. In my experience, even larger packages such as [naglebra](https://docs.rs/nalgebra/latest/nalgebra/) have been fast to install. To check the documentation of all packages installed locally, you can also use `cargo doc --open`, which is great for offline development. There are also good resources online when you're feeling stuck, like the [Rust Programming Language Book](https://doc.rust-lang.org/book/), or the more practical [Rust by Example](https://doc.rust-lang.org/stable/rust-by-example/). 


## Things I don't like (yet)

**Efficiency.** Rust takes longer to write. Probably, due to my lack of experience. I get the impression programs need to be better thought out. You'll take longer to write code, but it will be more _effective_ code. This makes Rust great for production. However, it's hard to think of Rust as a good language to experiment, explore, or even iterate quickly. Experimentation is a great advantage of languages like Python or JavaScript. It's a trade-off. 

**Types.** I like types. I've been using types in most of my Python production applications. Not only that, but I believe I now understand better why Python doesn't _enforce_ types. Types help you write more _correct_ programs, but it's easy to get stuck in type hell. I don't know if I want a `usize` or an `int32`. I don't care if it's a `Matrix` or a `DMatrix`, or `f32` or `f64`. The Rust compiler does. When I'm focused on solving a problem, I'm not interested in solving a _type_ problem. Types are great. But if you get too strict about them, types can get in the way. I felt Rust types got in the way a lot of times.
 
**Ecosystem.** Rust's ecosystem is still young. Yes, AoC puzzles are very specific and don't represent the real world. But when looking for libraries, for example, it appears Rust is still trying to figure out where does lie. This is normal. There are not that many resources on the internet _yet_. For a beginner programmer in any language, the quality of web resources is everything. When looking for answers and resources on Rust, it takes longer to find the right resources. When looking for libraries, it's tough to understand which libraries are the most popular ones, or the ones to go from. Even though things are developing [quickly](https://lib.rs/). 

```rust
struct Vector3 {
    x: f32,
    y: f32,
    z: f32
}

fn dot_product(a: Vector3, b: Vector3) -> float {
    a.x*b.x + a.y*b.y + a.z*b.z
}

fn do_math_by_copy(p1: Vector3, p2: Vector3, d1: Vector3, d2: Vector3, s: f32, t: f32) -> f32 {
    let a = p1 + s*d1;
    let b = p2 + s*d2;
    dot_product(b - a, b - a)
}

fn do_math_by_borrow(p1: &Vector3, p2: &Vector3, d1: &Vector3, d2: &Vector3, s: f32, t: f32) -> f32 {
    let a = p1 + &(&d1*s);
    let b = p2 + &(&d2*t);
    let result = dot_product(&(&b - &a), &(&b - &a));
}
```

**Borrowing.** References and borrowing have been the hardest concepts to grasp for me. Again. This might be very well due to my lack of experience in compiled languages. Look at the example above, taken from [this](https://www.forrestthewoods.com/blog/should-small-rust-structs-be-passed-by-copy-or-by-borrow/) great post. There is no obvious reason why you would go with `do_math_by_borrow`. It's uglier, less readable, and to the best of my knowledge, _not_ significantly faster. This whole borrowing and ownership dance is probably necessary for Rust. But I felt like doing a lot of `.Clone()` and `.Copy()` to escape this problem. 

## Closing thoughts

AoC was great to learn a new language! Perhaps next year something easier though. I didn't finish all the puzzles [by any means](https://github.com/duarteocarmo/advent2022/). But by day 10, I had a good grasp of the basics of Rust and could write simple programs without too much hassle. The problem with AoC is the steep curve in puzzle difficulty. By day 15, I was already spending one hour just to parse the input correctly. 

I can understand why Rust is loved. It's fast, effective, and it makes you a better programmer. It requires you to make deliberate choices on every variable you create, and every statement you write. This is a double-edged sword. On one side, it makes you write better and safer code. On the other side, it makes you write code slower, and experiments should be fast. It does look great for production. But it's [early](https://mdwdotla.medium.com/using-rust-at-a-startup-a-cautionary-tale-42ab823d9454) still. 

I would love to try and write some Machine Learning APIs in Rust. Written in Rust, they might be safer and faster! But for that to happen, I would need to be able to load models using Rust. This means loading Scikit, Transformer, or even PyTorch models with Rust. I don't think we are there yet. But when we are, I would love to give it a go. 