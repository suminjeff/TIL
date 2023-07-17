
# 마크다운 언어(Markdown Language)

---

## 1. 헤더(Headings)

> # Heading level 1
> ## Heading level 2
> ### Heading level 3
> #### Heading level 4
> ##### Heading level 5
> ###### Heading level 6

---

## 2. 문단(Paragraphs)

To create paragraphs, use a blank line to separate one or more lines of text.

Like this!

&nbsp;&nbsp;&nbsp;If you want to indent your paragraph, use `&nbsp;`. Each `&nbsp;` will replace one whitespace.

---

## 3. 줄바꿈(Line breaks)

To break a line or create a new line, end a line with 2 or more spaces, and press enter.  
Like this!  
However this may be confusing since it's hard to see the whitespaces in your editor.<br>For this reason, using the `<br>` HTML tag may be useful.

---

## 4. 글자 스타일(Emphasis)

1. 굵게(Bold)
- Use two astericks(**) before and after the word/phrase to bold.
- **Like this!**

2. 기울이기(Italic)
- Use one asterick(*) before and after the word/phrase to italicize.
- *Like this!*

3. 굵게 + 기울이기(Bold and Italic)
- Use three astericks(***) before and after the word/phrase to bold and italicize at the same time.
- ***Like this!***

4. 취소선(Strikethrough)
- Use two tildes(~~) before and after the word/phrase to strikethrough.
- ~~Like this!~~

---

## 5. 인용문(Blackquotes)
> Use blackquotes with right angle brackets.
> Like this!
>> You can use double brackets to nest the blackquote.
> #### You can use other elements in the blackquote area.
> *Like* **this!**

---

## 6. 리스트(Lists)

1. 순서가 있는 리스트(Ordered Lists)
Simply number the line items you wish to list orderly.
1. One
2. Two
3. Three

2. 순서가 없는 리스트(Unordered Lists)
Use dashes(-), astericks(*) or plus signs(+) in front of line items.
- Things to buy
  - Rice
  - Meatloaf
  - Bread

---

## 7. 코드블럭 (Code Blocks)
- Use three backticks(```) to create code blocks.
  
```python
print('Like this!')
```

- Make sure to write the correct language for the code.
  
```javascript
console.log('This is javascript')
```

- Use braces({}) to fence the code block

```
{
  "firstName" : "John",
  "lastName" : "Smith",
  "age" : 25
}
```

---

## 8. 링크/이미지 (Link/Images)
- Link format : `[keyword](url "optional title")`

[Dog API](https://dog.ceo/dog-api/ "Dog API")

- Image format : `![alt text](path)`

![Puppy](https://images.dog.ceo/breeds/collie-border/n02106166_1246.jpg)

---
