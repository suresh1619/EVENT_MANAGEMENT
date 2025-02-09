import React, { useState } from 'react';
import axios from 'axios';
import ReactMarkdown from 'react-markdown';
import styled from 'styled-components';

const Container = styled.div`
  width: 80%;
  margin: 0 auto;
  padding: 20px;
  background-color: #f9f9f9;
  border-radius: 8px;
`;

const Input = styled.input`
  width: 100%;
  padding: 10px;
  margin-bottom: 10px;
  border: 1px solid #ccc;
  border-radius: 4px;
`;

const Button = styled.button`
  width: 100%;
  padding: 10px;
  background-color: #4CAF50;
  color: white;
  border: none;
  border-radius: 4px;
  cursor: pointer;
  &:hover {
    background-color:rgb(162, 225, 166);
  }
`;

const Summary = styled.div`
  margin-top: 20px;
`;

function QueryComponent() {
  const [query, setQuery] = useState('');
  const [response, setResponse] = useState(null);

  const handleQuery = async () => {
    try {
      const res = await axios.post('http://127.0.0.1:8000/', { query }, {
        headers: { 'Content-Type': 'application/json' },
      });
      setResponse(res.data);
    } catch (error) {
      console.error('Error fetching data:', error);
    }
  };

  return (
    <Container>
      <Input
        type="text"
        value={query}
        onChange={(e) => setQuery(e.target.value)}
        placeholder="Enter your query"
      />
      <Button onClick={handleQuery}>Submit</Button>

      {response && (
        <Summary>
          <h3>Chatbot:</h3>
          <ReactMarkdown>
            {response.summary}
          </ReactMarkdown>
        </Summary>
      )}
    </Container>
  );
}

export default QueryComponent;
