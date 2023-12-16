import { Head, Html, Main, NextScript } from "next/document"
import Script from "next/script"



export default function Document() {
  return (
    <Html>
  <Head>
  <Script src={`https://www.googletagmanager.com/gtag/js?id=G-4T7C8ZD9TR`} strategy={`afterInteractive`}/>
  <Script strategy={`afterInteractive`}>
  {`
window.dataLayer = window.dataLayer || [];
function gtag(){window.dataLayer.push(arguments);}
gtag('js', new Date());
gtag('config', 'G-4T7C8ZD9TR');
`}
</Script>
</Head>
  <body>
  <Main/>
  <NextScript/>
</body>
</Html>
  )
}
