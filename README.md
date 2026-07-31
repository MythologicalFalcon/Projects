# Projects

Seven standalone projects. Each directory is self-contained.

## 1. Angular

A movie browsing single-page app on Angular 18 with server-side rendering. Standalone
components, the Angular router, and RxJS for async data. Bootstrap 5 and SCSS for
styling, Express hosting the SSR build.

Angular 18, TypeScript, RxJS, Angular SSR, Express, Bootstrap 5, SCSS.

## 2. ChatGeneration

A Flask chatbot that answers from a custom intent set built for an organisation. It
holds two approaches in one codebase: an NLTK and tflearn intent classifier trained on
`intents.json`, and generative responses through Vertex AI and the Google Generative AI
API. Firebase Admin handles persistence.

Python, Flask, TensorFlow, tflearn, NLTK, Vertex AI, Google Generative AI, Firebase Admin.

## 3. PictureCodingAnalysis

Three notebooks on image compression and source coding. Huffman coding and Shannon-Fano
coding built from symbol frequencies over greyscale images, plus a compressive sensing
reconstruction with a recovered-image comparison.

Python, NumPy, matplotlib, Jupyter.

## 4. StockMarketAnalysisKafka

A Kafka producer and consumer pair that streams stock index data and writes it out to
S3. Roughly 100 lines. It is a streaming exercise rather than a service.

Python, kafka-python, pandas, boto3, s3fs.

## 5. TestCaseReduction

Reduces a regression test suite by grouping test cases on their numeric features with
scikit-learn `NearestNeighbors`, then writing out the reduced set and a report. The aim
is shorter test runs at comparable coverage.

Python, scikit-learn, pandas, matplotlib.

## 6. TimesheetManagement

A Flask and MySQL timesheet app. Employees log time and managers review it. Login is
protected by TOTP two-factor auth using pyotp, with codes delivered over SMTP, and the
views are separated by role.

Python, Flask, MySQL, pyotp, smtplib, HTML, CSS.

## 7. Uber Data Analytics

A Mage.ai ETL pipeline that extracts an Uber trip dataset, transforms it into a
dimensional model of fact and dimension tables, and loads it into BigQuery for querying.
Built by following a public tutorial.

Python, Mage.ai, pandas, Google BigQuery, SQL.
