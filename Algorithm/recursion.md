# recursion

### 무한 루프

- 무한 루프를 주의한다.
    - java.lang.StackOverflowError 가 발생한다.
    - 분기 등을 통해 적절한 제동을 걸어준다.
        
        ```java
        public class Code {
            public static void main(String[] args) {
                func(4);
            }
            public static void func(int k) {
                if (k<=0) return; // Base case
                else {
                    System.out.println("Hello...");
                    func(k-1); // Recursive case
        						// if func(k+1) 이면 결국 무한루프에 빠진다. Recursive case가 충족되지 않음.
                }
            }
        }
        ```
        
    - 조건
        - **Base case** : 적어도 하나의 recursion에 빠지지 않는 경우가 존재해야 한다.
        - Recursive case : recursion을 반복하다 보면, 결국 base case로 수렴해야 한다.

### 순환 함수와 수학적 귀납법

순환 함수를 수학적 귀납법을 통해 논리적으로 생각해보며 이해할 수 있다.

```java
public static int func(int k) {
      // Base case
      if (k==0) return 0; 
      else {
          // Recursive case
          return k + func(k-1);
      }
}
```

- func(int n)은 음이 아닌 정수 n에 대해 0에서 n까지의 합을 계산한다.
    1. n = 0 인 경우,  0을 반환하므로 올바르다.
    2. n < k 인 경우, 0에서 n까지의 합을 올바로 계산한다고 가정한다.
    3. n = k인 경우, func(k) 는 k + func(k-1)을 반환하며, 2의 가정에 의해서 func(k-1)은 올바른 합을 계산해 반환하므로, 결과적으로 func(k)의 결과는 0부터 k까지의 합을 계산한는 것이 성립한다.

### Factorial : n!

- 0! = 1
- n! = n * (n-1)! , n>0

```java
public static int factorial(int n) {
    if (n==0)  return 1;
    else return n * factorial(n-1);
}
```

- 수학적 귀납법
    - factorial(int n)은 음이 아닌 정수 n에 대해서 n!을 계산한다.
        1. n = 0 인 경우, 1을 반환하므로 올바르다.
        2. n < k 인 경우, n!을 계산한 값을 반환한다고 가정한다.
        3. n = k 인 경우, factorial(k)는  k * factorial(k)를 반환한다. 2의 가정에 의해서 factorial(k-1)은 (k-1)!을 계산한 값을 반환하므로, factorial(k)는 k * (k-1)! = k!을 계산하여 반환하게 된다. 즉, 가정이 성립한다.

### Power

- x^0 = 1
- x^n = x * x^(n-1) , if n>0

```java
public static double power(double x, int n) {
    if (n == 0) return 1;
    else return x * power(x, n-1);
}
```

### Fibonacci Number

- f0 = 0
- f1 = 1, f2 = 1
- fn = fn-1 + fn-2 , n>1

```java
public static int fibonacci(int n) { // n이 음수가 아니라고 가정
    if (n<2) return n;
    else return fibonacci(n-1) + fibonacci(n-2);
}
```

### Euclid Method (최대 공약수)

- 두 양의 정수 m과 n (m ≥ n)에 대해서, m이 n의 배수이면, gcd(m, n) = n이고, 그렇지 않으면 gcd(m, n) = gcd(n, m%n)이다.

```java
public static int gcd(int m, int n) {
    if(m<n) {
        int tmp = m; m = n; n = tmp;
    } // 조건에 맞게 swap m and n

    if(m%n==0) return n;
    else return gcd(n, m%n);
}
```

- 단순한 버전
    - gcd(p, q) = p , if q=0
    - gcd(q, p%q) , otherwise

```java
public static int gcd2(int p, int q) {
    if(q==0) return p;
    else return gcd(q, p%q); 
}
```

#### 출처
- 유튜 권오흠 교수님, 알고리즘 강의(2015)