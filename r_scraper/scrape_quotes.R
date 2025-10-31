library(rvest)
library(readr)
library(dplyr)

url <- "http://quotes.toscrape.com/"
page <- read_html(url)

quotes <- page %>% html_nodes(".text") %>% html_text(trim = TRUE)
authors <- page %>% html_nodes(".author") %>% html_text(trim = TRUE)

df <- tibble(quote = quotes, author = authors)
write_csv(df, "quotes_r.csv")

print(head(df))
