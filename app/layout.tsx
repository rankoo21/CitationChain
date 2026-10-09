import type {Metadata} from 'next';import './globals.css';
export const metadata:Metadata={title:'CitationChain — Research Provenance',description:'Three-source artifact quorum on GenLayer Studionet.'};
export default function RootLayout({children}:{children:React.ReactNode}){return <html lang="en"><body>{children}</body></html>}

