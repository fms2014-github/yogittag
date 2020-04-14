<template>
    <div>
        <b-table
            :items="items"
            :fields="fields"
            table-variant="light"
            head-variant="light"
            responsive="sm"
        ></b-table>
    </div>
</template>

<script>
export default {
    props: {
        fields: {
            type: Array,
            default: function () {
                return [
                    {
                        key: 'last_name',
                        sortable: true,
                    },
                    {
                        key: 'first_name',
                        sortable: false,
                    },
                    {
                        key: 'age',
                        label: 'Person age',
                        sortable: true,
                    },
                ]
            },
        },
        items: {
            type: Array,
            default: function () {
                return [
                    { age: 40, first_name: 'Dickerson', last_name: 'Macdonald' },
                    { age: 21, first_name: 'Larsen', last_name: 'Shaw' },
                    { age: 89, first_name: 'Geneva', last_name: 'Wilson' },
                    { age: 38, first_name: 'Jami', last_name: 'Carney' },
                ]
            },
        },
    },
}
</script>
