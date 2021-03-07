import React from "react";

import { useTable, useFilters, usePagination} from 'react-table'
import 'bootstrap/dist/css/bootstrap.min.css';

// Define a default UI for filtering

function DefaultColumnFilter({
    column: { filterValue, preFilteredRows, setFilter },
}) {
    const count = preFilteredRows.length

    return (
        <input
            className="form-control"
            value={filterValue || ''}
            onChange={e => {
                setFilter(e.target.value || undefined)
            }}
            placeholder={`Search ${count} records...`}
        />
    )
}

function Table({ columns, data }) {

    const defaultColumn = React.useMemo(
        () => ({
            // Default Filter UI
            Filter: DefaultColumnFilter,
        }),
        []
    )

    const {
        getTableProps,
        getTableBodyProps,
        headerGroups,
        page,
        prepareRow,
        canPreviousPage,
        canNextPage,
        pageOptions,
        pageCount,
        gotoPage,
        nextPage,
        previousPage,
        setPageSize,
        state: { pageIndex, pageSize },
    } = useTable(
        {
            columns,
            data,
            defaultColumn,
            initialState: { pageIndex: 0 },
        },
        useFilters,
        usePagination
    )

    return (
        <div>
            <table className="table table-sm" {...getTableProps()}>
                <thead>
                    {headerGroups.map(headerGroup => (
                        <tr {...headerGroup.getHeaderGroupProps()}>
                            {headerGroup.headers.map(column => (
                                <th {...column.getHeaderProps()}>
                                    {column.render('Header')}
                                    {/* Render the columns filter UI */}
                                    <div>{column.canFilter ? column.render('Filter') : null}</div>
                                </th>
                            ))}
                        </tr>
                    ))}
                </thead>
                <tbody {...getTableBodyProps()}>
                    {page.map((row, i) => {
                        prepareRow(row)
                        return (
                            <tr {...row.getRowProps()}>
                                {row.cells.map(cell => {
                                    return <td {...cell.getCellProps()}>{cell.render('Cell')}</td>
                                })}
                            </tr>
                        )
                    })}
                </tbody>
            </table>
            <br />
            <div className="pagination">
                <button onClick={() => gotoPage(0)} disabled={!canPreviousPage}>
                {'<<'}
                </button>{' '}
                <button onClick={() => previousPage()} disabled={!canPreviousPage}>
                {'<'}
                </button>{' '}
                <button onClick={() => nextPage()} disabled={!canNextPage}>
                {'>'}
                </button>{' '}
                <button onClick={() => gotoPage(pageCount - 1)} disabled={!canNextPage}>
                {'>>'}
                </button>{' '}
                <span>
                Page{' '}
                <strong>
                    {pageIndex + 1} of {pageOptions.length}
                </strong>{' '}
                </span>
                <span>
                | Go to page:{' '}
                <input
                    type="number"
                    defaultValue={pageIndex + 1}
                    onChange={e => {
                    const page = e.target.value ? Number(e.target.value) - 1 : 0
                    gotoPage(page)
                    }}
                    style={{ width: '100px' }}
                />
                </span>{' '}
                <select
                value={pageSize}
                onChange={e => {
                    setPageSize(Number(e.target.value))
                }}
                >
                {[10, 20, 30, 40, 50].map(pageSize => (
                    <option key={pageSize} value={pageSize}>
                    Show {pageSize}
                    </option>
                ))}
                </select>
            </div>
        </div>
    )
}



function FilterTableComponent() {
    const columns = React.useMemo(
        () => [
            {
                Header: 'Vehicle',
                columns: [
                    {
                        Header: 'Model',
                        accessor: 'carModel',
                    },
                    {
                        Header: 'Version',
                        accessor: 'carVersion'
                    },
                ],
            },
            {
                Header: 'Section Times',
                columns: [
                    {
                        Header: 'Starting Point',
                        accessor: 'startPoint'
                    },
                    {
                        Header: 'Ending Point',
                        accessor: 'endPoint'
                    },
                    {
                        Header: 'Status',
                        accessor: 'status'
                    },
                    {
                        Header: 'Duration (seconds)',
                        accessor: 'duration'
                    },
                ],
            },
        ],
        []
    )

    const data = [
        {
            "carVersion": "C1_V5",
            "carModel": "C1",
            "startPoint": 'p_d',
            "endPoint": 'p_r_23',
            "status": 'Speeding',
            "duration": 3.123124
        },
        {
            "carVersion": "C2_V4",
            "carModel": "C2",
            "startPoint": 'p_s_a',
            "endPoint": 'p_r_26',
            "status": 'Absent',
            "duration": 5.4
        },
        {
            "carVersion": "C1_V5",
            "carModel": "C1",
            "startPoint": 'p_d',
            "endPoint": 'p_r_23',
            "status": 'Normal',
            "duration": 7.6
        },
        {
            "carVersion": "C5_V5",
            "carModel": "C5",
            "startPoint": 'p_s_a',
            "endPoint": 'p_t',
            "status": 'Queueing',
            "duration": 8.5
        }
    ]

    return (
        <Table columns={columns} data={data} />
    )
}

export default FilterTableComponent;