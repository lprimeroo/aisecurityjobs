import React, { useState, useEffect } from 'react';
import { TypeAnimation } from 'react-type-animation';
import { InputText } from 'primereact/inputtext';
// import { Button } from 'primereact/button';
import { DataTable } from 'primereact/datatable';
import { Column } from 'primereact/column';
import axios from 'axios';
import 'primereact/resources/themes/saga-blue/theme.css';
import 'primereact/resources/primereact.min.css';
import 'primeicons/primeicons.css';
import 'primeflex/primeflex.css';
import './App.css';

function Title() {
  const titles = ["AI", "ML", "ML Infra", "LLM", "GenAI"];
  return (
    <div className="p-grid p-justify-center title">
      <div className="p-col-12 p-text-center">
        <h1>
          <TypeAnimation 
            cursor={true}
            sequence={titles.map(title => `${title} Security Jobs`)}
            wrapper="text"
            speed={{type: 'keyStrokeDelayInMs', value: 125}}
            repeat={Infinity}
            delay={1500} // delay between typing different titles
          />
        </h1>
      </div>
    </div>
  );
}

function SearchBar({ onSearch }) {
  const [query, setQuery] = useState('');

  useEffect(() => {
    onSearch(query);
  }, [query, onSearch]);

  return (
    <div className="p-grid p-justify-center search-bar">
      <div className="p-col-12 p-md-6">
        <InputText
          placeholder="Search jobs"
          value={query}
          onChange={(e) => setQuery(e.target.value)}
        />
      </div>
    </div>
  );
}

function JobsTable({ jobs }) {
  return (
    <DataTable value={jobs} className="p-datatable-sm">
      <Column field="id" header="ID" />
      <Column field="title" header="Title" />
      <Column field="description" header="Description" />
    </DataTable>
  );
}

function App() {
  const [jobs, setJobs] = useState([]);

  useEffect(() => {
    axios.get('http://localhost:5000/jobs').then((response) => {
      setJobs(response.data);
    });
  }, []);

  const handleSearch = (query) => {
    const url = query ? `http://localhost:5000/jobs/search?q=${query}` : 'http://localhost:5000/jobs?page=1&per_page=10';
    axios.get(url).then((response) => {
      setJobs(response.data);
    });
  };

  return (
    <div className="p-grid p-justify-center p-align-center app-container">
      <div className="p-col-12">
        <Title />
      </div>
      <div className="p-col-12">
        <SearchBar onSearch={handleSearch} />
      </div>
      <div className="p-col-12 p-md-8">
        <JobsTable jobs={jobs} />
      </div>
    </div>
  );
}

export default App;