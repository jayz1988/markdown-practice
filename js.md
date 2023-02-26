# JS

## = 연산자
== 동등
=== 일치

## 참과 거짓(Truthly & Falsy)

1) false
2) 0
3) null
4) undefined
5) NaN
6) ''
7) 0n

## 데이터 타입 확인

```javascript
console.log(typeof 'a' === 'string')
console.log(typeof 123 === 'number')
console.log(typeof false === 'boolean')
console.log(typeof undefined === 'undefined')
console.log(typeof null === 'object') // 구분 안됨
console.log(typeof [] === 'object') // 구분 안됨
console.log(typeof {} === 'object') // 구분 안됨
console.log(typeof function () {} === 'function')

// console.log(null.constructor)
console.log([].constructor === Array)
console.log({}.constructor === Object)

console.log(Object.prototype.toString.call(null).slice(8,-1) === 'Null')

function checkType(data) {
  return Object.prototype.toString.call(data).slice(8,-1)
}
console.log(checkType({}))
```
## 논리
```javascript
// 논리(Logical)

const a = true
const b = false

// AND(그리고) 연산자
// 가장 먼저 만나는 falsy data를 반환. 뒤쪽 data는 그냥 넘어감
// falsy data가 없으면 가장 뒤쪽 data를 반환함

if (a && b) {
  console.log('모두가 참!')
}

// OR(또는) 연산자
// 가장 먼저 만나는 truesy data를 반환. 뒤쪽 data는 그냥 넘어감
// truesy data가 없으면 가장 뒤쪽 data를 반환함
if (a || b) {
  console.log('하나 이상이 참!')
}

// Nullish 병합 연산자를 사용한 경우
// null, undefined를 건너뛰고, 다른 data를 반환
const num2 = n ?? 7
console.log(num2)

// 삼항 (Ternary)
// 조건 ? 참 : 거짓
console.log(a < 2 ? '참!' : '거짓...')
```
## 전개 연산자
```javascript
// 전개 연산자(Spread Operator)

const a = [1,2,3]
const b = [4,5,6]

const c = a.concat(b)
console.log(c)

const d = [...a,...b]
console.log(d) // [1,2,3,4,5,6]

const aa = {x:1 , y:2}
const bb = {y:3 , z:4}

const cc = Object.assign({}, aa, bb)
console.log(cc)

const dd = {...aa, ...bb}
console.log(dd)

function fn(x,y,z) {
  console.log(x,y,z)
}

fn(1,2,3)

const aaa = [1,2,3]
// fn(aaa[0], aaa[1], aaa[2])
// fn(a)
fn(...a)
```

## 구조 분해 할당
```javascript
const obj = {
  a: 1,
  b: 2,
  c: 3,
  x: 7,
  y: 100
};

const { c, ...rest } = obj

console.log(c, rest)
```
## 선택적 체이닝
```javascript
const userA = {
  name:'heropy',
  age:85,
  address: {
    country: 'Korea',
    city: 'Seoul'
  }
}
const userB = {
  name: 'Neo',
  age: 22
}

function getCity(user) {
  return user.address?.city || '주소 없음.'
}

console.log(getCity(userA))
console.log(getCity(userB))
```

## if 조건문
```javascript
if (조건) {
  //
}

if (조건) {
  //
} else {
  //
}

if (조건1) {
  //
} else if (조건2) {
  //
} else if (조건3) {
  //
} else {
  //
}
```

## switch 조건문
```javascript
switch (조건) {
  case 값1:
    // 조건이 값1일 때 실행
    break
  case 값2:
    // 조건이 값2일 때 실행
    break
  default:
    // 조건이 값1도 값2도 아닐 때 실행
    break
}
```

## for 반복문
```javascript
for (초기화; 조건; 증감) {
  // 반복 실행할 코드
}
// continue : 이번 반복은 넘어가고 다음 반복 실행
for (let i = 9; i > -1; i -= 1) {
  if ( i % 2 === 0 ) {
    continue
  }
  console.log(i)
}
```
## for of 반복문
```javascript
for (const a of fruits) {
  console.log(a)
}
```
## for in 반복문
```javascript
const user = {
  name: 'heropy',
  age: 85,
  isValid: true,
  email: 'aaa@aaa.aa'
}

for (const key in user) {
  console.log(key + ' : ' + user[key])
}
```
## While 반복문
```javascript
let n = 0
while (n < 4) {
  console.log(n)
  n += 1
}
```
## Do While 조건문
```javascript
// 처음조건이 falsy여도 한번은 실행이 되도록
let n = 0
// while (n) {
//   console.log(n)
// }
do {
  console.log(n)
  n += 1
} while (n < 4)
```
## 함수
### 선언과 표현 그리고 호이스팅

```javascript
// 함수

// 함수 선언문
// function hello () {}

// 함수 표현식
// const hello = function () {}

// 호이스팅
// 함수 선언 시 순서 상관없이 호출 가능, 함수 표현 시 순서 고려하여 작성해야 함
hello()

function hello () {
  console.log('Hello~')
}

const hello = function () {
  console.log('Hello~')
}
```
### 매개변수 패턴
```javascript
// 매개변수 패턴
//// 기본값

function sum(a, b = 1) {
  return a + b
}

console.log(sum(1, 2))
console.log(sum(7))

//// 구조 분해 할당

const user = {
  name: 'heropy',
  age:85,
  email: 'aaa@aaa.aa'
}

function getName({name}) {
  return name
}
function getEmail({email = '이메일이 없습니다.'}) {
  return email
}

console.log(getName(user))
console.log(getEmail(user))

const fruits = ['Apple', 'Banana', 'Cherry']
const numbers = [1,2,3,4,5,6,7]

function getSecondItem([, b]) {
  return b
}
console.log(getSecondItem(fruits))
console.log(getSecondItem(numbers))

function sum(...rest) {
  console.log(rest)
  // console.log(arguments) === Array.like
  return rest.reduce(function (acc, cur) {
    return acc + cur
  }, 0)
}
console.log(sum(1,2)) // 3
console.log(sum(1,2,3,4)) // 10
console.log(sum(1,2,3,4,5,6,7,8,9,10)) // 55
```
### 화살표 함수
```javascript
const a = () => {}
const b = x => {}
const c = (x,y) => {}

const d = x => {return x * x}
const e = x => x * x

const f = x => {
  console.log(x*x)
  return x*x
}

const g = () => { return { a : 1 }}
const h = () => ({ a : 1 })
const i = () => { return [1,2,3]}
const j = () => [1,2,3]

```
### 즉시실행함수
```javascript
;(() => {})()  // (f)()
;(function () {})()  // (f)()
;(function () {}())  // (f())
;!function () {}()  // !f()
;+function () {}()  // +f()
```
# 콜백
```javascript
// 하나의 함수를 다른 함수의 인수로 집어넣어 불러오는 것
const sum = (a, b, c) => {
  setTimeout(() => {
    c(a + b)
  }, 1000)
}
sum(1, 2, value => {
  console.log(value)
})
sum(3, 7, value => {
  console.log(value)
})

// 실전
// https://www.gstatic.com/webp/gallery/4.jpg
const loadImage = (url, cb) => {
  const imgEl = document.createElement('img')
  imgEl.src = url
  imgEl.addEventListener('load', () => {
    setTimeout(() => {
      cb(imgEl)
    }, 1000)
  })
}

const containerEl = document.querySelector('.container')
loadImage('https://www.gstatic.com/webp/gallery/4.jpg', imgEl => {
  containerEl.innerHTML = ''
  containerEl.append(imgEl)
})
```
### 재귀
```javascript
// 함수 내부에서 다시 함수를 실행
const userA = {
  name: "A",
  parent: null
}
const userB = {
  name: "B",
  parent: userA
}
const userC = {
  name: "C",
  parent: userB
}
const userD = {
  name: "D",
  parent: userC
}


const getRootUser = user => {
  if (user.parent) {
    return getRootUser(user.parent)
  }
  return user
}

console.log(getRootUser(userD))
```
### 호출 스케줄링
```javascript
//setInterval, setTimeout
const hello = () => {
  console.log('Hello~')
}
const timeout = setInterval(hello, 2000);
const h1El = document.querySelector('h1')
h1El.addEventListener('click', () => {
  console.log('Clear!')
  clearInterval(timeout)
})
```
### this
```javascript
// this
//// 일반 함수의 this는 호출 위치에서 정의
//// 화살표 함수의 shit는 자신이 선언된 함수(렉시컬) 범위에서 정의

function user() {
  this.firstName = 'Neo' 
  this.lastName = 'Anderson'

  return {
    firstName: 'Heropy',
    lastName: 'Park',
    age:85,
    getFullName () {
      return `${this.firstName} ${this.lastName}`
    }
  }
}

const lewis = {
  firstName: 'Lewis',
  lastName: 'Yang'
}

const u = user()
console.log(u.getFullName())
console.log(u.getFullName.call(lewis))







const timer = {
  title: 'TIMER!',
  timeout() {
    console.log(this.title)
    setTimeout(() => {
      console.log(this.title)
    }, 1000)
  }
}
timer.timeout()
```
