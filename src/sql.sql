SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_table_access_method = heap;

CREATE TABLE public.nfts (
    nft_address character varying,
    nft_metadata character varying
);
ALTER TABLE public.nfts OWNER TO postgres;
CREATE TABLE public.testvalues (
    randomstring character varying(50)
);


ALTER TABLE public.testvalues OWNER TO postgres;

COPY public.nfts (nft_address, nft_metadata) FROM stdin;
KWWugGMUt7x1iqf0sAjQK9LlRa92jROvaX37DcMZjiiDxtfW4pX04TArIYE6JpZw	{"mint":"3LZ9ezL5BkCtvdVGLkrw1q633EgfeYDpgGtBgWDgmaSU","standard":"metaplex","name":"Baby Yetis #257","symbol":"","metaplex":{"metadataUri":"https://arweave.net/4PtHGFuAw2U-T4nrIWVRxJ0EpVIivRWi4xjreBkmMVg","updateAuthority":"yeT3ik5jX5RuK8JF8P3RRHrr9g6ox6RMWbRMh3r9FxQ","sellerFeeBasisPoints":500,"primarySaleHappened":0,"owners":[{"address":"64eiSEPv2KRKNkPAX6d4BZQ3b12PcFqZP2yPoNAZw9po","verified":0,"share":100},{"address":"yeT3ik5jX5RuK8JF8P3RRHrr9g6ox6RMWbRMh3r9FxQ","verified":1,"share":0}],"isMutable":true,"masterEdition":false}}
\.

COPY public.testvalues (randomstring) FROM stdin;
